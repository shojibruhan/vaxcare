from django.urls import path, include
from users.views import DoctorViewSet, PatientViewSet
# from users import views
from campaigns.views import VaccineViewSet, BookingViewSet

from rest_framework_nested import routers
from review.views import DoctorReviewViewSet, CampaignReviewViewSet

router= routers.DefaultRouter()
router.register('doctors', DoctorViewSet, basename='doctor')
router.register('patients', PatientViewSet, basename='patient')
router.register('vaccines', VaccineViewSet, basename='vaccines')
router.register('bookings', BookingViewSet, basename='booking')
# router.register('review', CampaignReviewViewSet, basename='review')
doctor_router= routers.NestedDefaultRouter(router, 'doctors', lookup='doctor')
doctor_router.register('reviews', DoctorReviewViewSet, basename='doctor-review')

vaccine_router= routers.NestedDefaultRouter(router, 'vaccines', lookup= 'vaccine')
vaccine_router.register('reviews', CampaignReviewViewSet, basename='campaign-review')



urlpatterns = [
    path('', include(router.urls)),
    path('', include(doctor_router.urls)),
    path('', include(vaccine_router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
