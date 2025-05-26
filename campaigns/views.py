from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.conf import settings as main_settings
from .models import Vaccine, Booking
from users.models import Patient
from .serializers import CreateVaccineSerializers ,VaccineSerializers, BookingSerializers, BookListSerializers
from .filters import VaccineFilterset, BookingFilterset
from rest_framework import status
from review.permissions import IsReviewAuthorOrReadOnly
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin, ListModelMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser, IsAuthenticated
from rest_framework.decorators import api_view
from sslcommerz_lib import SSLCOMMERZ 
from rest_framework.response import Response
from rest_framework.views import APIView




class VaccineViewSet(ModelViewSet):
    # queryset= Vaccine.objects.all()
    # serializer_class= VaccineSerializers
    filter_backends= [DjangoFilterBackend, SearchFilter]
    filterset_class= VaccineFilterset
  


    def get_queryset(self):
        queryset= Vaccine.objects.select_related('doctor__user')
        if self.request.user.is_staff:
            return queryset.all()
        # if hasattr(self.request.user, 'doctor'):
        if self.request.user.is_authenticated and hasattr(self.request.user, 'doctor'):
            return queryset.filter(doctor= self.request.user.doctor)
       
        # return queryset.none()
        return queryset
  


    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateVaccineSerializers
        return VaccineSerializers
    
    def get_serializer_context(self):
        if hasattr(self.request.user, 'doctor'):
            return {'doctor_id': self.request.user.doctor.id}
        
    # def get_permissions(self):
    #     if self.request.method in ['POST', 'PATCH', 'DELETE']:
    #         return [IsAdminUser()]
    #     return [IsAuthenticated()]

class BookingViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
# class BookingViewSet(ModelViewSet):
    # http_method_names=['get', 'put', 'patch', 'post', 'delete']
    queryset= Booking.objects.all()
    # serializer_class= BookingSerializers
    permission_classes= [IsAuthenticated]
    
    # def get_queryset(self):
    #     if self.request.user.is_staff:
    #         return Booking.objects.select_related('patient__user', 'vaccine__doctor')
    #     return Booking.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return BookListSerializers
        return BookingSerializers

   

    def get_serializer_context(self):
        if not self.request.user.is_authenticated:
            return {}
        # return {'patient_id': self.request.user.patient.id, 'user_id': self.request.user.id}
        return {'patient_id': self.request.user.patient.id}


class BookListViewSet(ModelViewSet):
    """
    # List of Booked/appointed vaccine by patiet
        - Admin user can view all the list
        - Authenticate user(patient can view only if booked a vaccine campaign)
    """
    serializer_class= BookListSerializers
    filter_backends= [SearchFilter]
    search_fields= ['status']
    http_method_names= ['get']
    # permission_classes= [IsAuthenticated]

    def get_queryset(self):
        queryset = Booking.objects.select_related('patient__user', 'vaccine__doctor')
        if getattr(self, 'swagger_fake_view', False):
            return Booking.objects.none()
        if self.request.user.is_staff:
            return queryset.all()
        if self.request.user.is_authenticated:
            return queryset.filter(patient__user= self.request.user)
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookingSerializers
        return BookListSerializers
        
    # def get_serializer_context(self):
    #     return {'patient_id': self.request.user.patient.id, 'user_id': self.request.user.id}
    # def get_permissions(self):
    #     if self.request.method in ['PATCH', 'PUT', 'DELETE']:
    #         return [IsAdminUser()]
    #     return [IsAuthenticated()]

class HasVaccinated(APIView):
    permission_classes= [IsAuthenticated]

    def get(self, request, booking_id):
        user= request.user
        print("user: ", user)
        print("ID (booking): ", booking_id)

        try:
            patient = user.patient  # Only works if this user *is* a patient
            print("patient: ", patient)
        except Patient.DoesNotExist:
            return Response({"error": "User is not a patient."}, status=403)
        # data= Booking.objects.get(patient= user, id=booking_id)
        # print("data: ", data)
        
        has_vaccinated= Booking.objects.filter(patient= patient, id= booking_id).exists()
        return Response({"has_vaccinated": has_vaccinated})
    



@api_view(['POST'])
def initiate_payment(request):
    user= request.user
    amount= request.data.get("amount")
    booking_id= request.data.get("bookingId")
    # num_items= request.data.get("numItems")
    settings = { 
                'store_id': 'phima680bc9617995d', 
                'store_pass': 'phima680bc9617995d@ssl', 
                'issandbox': True 
                }
    sslcz = SSLCOMMERZ(settings)
    post_body = {}
    post_body['total_amount'] = amount
    post_body['currency'] = "BDT"
    post_body['tran_id'] = f"trxn_{booking_id}"
    post_body['success_url'] = f"{main_settings.BACKEND_URL}/api/v1/payment/success/"
    post_body['fail_url'] = f"{main_settings.BACKEND_URL}/api/v1/payment/fail/"
    post_body['cancel_url'] = f"{main_settings.BACKEND_URL}/api/v1/payment/cancel/"
    post_body['emi_option'] = 0
    post_body['cus_name'] = f"{user.first_name} {user.last_name}"
    post_body['cus_email'] = user.email
    post_body['cus_phone'] = user.phone_number
    post_body['cus_add1'] = user.address
    post_body['cus_city'] = "Dhaka"
    post_body['cus_country'] = "Bangladesh"
    post_body['shipping_method'] = "NO"
    post_body['multi_card_name'] = ""
    # post_body['num_of_item'] = num_items
    post_body['product_name'] = "Vaccination Product"
    post_body['product_category'] = "Medicine"
    post_body['product_profile'] = "Helth Care"


    response = sslcz.createSession(post_body) # API response
    # print("response: ", response)

    # Need to redirect user to response['GatewayPageURL']
    if response.get("status") == 'SUCCESS':
        print("success status shows: ", response)
        return Response({"payment_url": response["GatewayPageURL"]})
        
    return Response({"error": "Payment initiation failed"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def payment_success(request):
    booking_id=request.data.get("tran_id").split('_')[1]
    booking=Booking.objects.get(id= booking_id)
    booking.status= "Completed"
    booking.save()

    # return HttpResponseRedirect(f"{main_settings.FRONTEND_URL}/dashboard/my-appointment")
    return HttpResponseRedirect(f"{main_settings.FRONTEND_URL}/dashboard/payment/success")

@api_view(['POST'])
def payment_cancel(request):
    return HttpResponseRedirect(f"{main_settings.FRONTEND_URL}/dashboard/my-appointment")


@api_view(['POST'])
def payment_fail(request):
    return HttpResponseRedirect(f"{main_settings.FRONTEND_URL}/dashboard/my-appointment")