from django.urls import path, include
from users.views import DoctorViewSet, PatientViewSet
# from users import views
from campaigns.views import VaccineViewSet, BookingViewSet

from rest_framework_nested import routers
from review.views import DoctorReviewViewSet

router= routers.DefaultRouter()
router.register('doctors', DoctorViewSet, basename='doctor')
router.register('patients', PatientViewSet, basename='patient')
router.register('vaccines', VaccineViewSet, basename='vaccines')
router.register('bookings', BookingViewSet, basename='booking')

doctor_router= routers.NestedDefaultRouter(router, 'doctors', lookup='doctor')
doctor_router.register('reviews', DoctorReviewViewSet, basename='doctor-review')



urlpatterns = [
    path('', include(router.urls)),
    path('', include(doctor_router.urls))
]
