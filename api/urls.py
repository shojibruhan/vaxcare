from django.urls import path, include
# from users.views import DoctorViewSet, PatientViewSet
from users import views
from rest_framework_nested import routers
from review.views import DoctorReviewViewSet

router= routers.DefaultRouter()
router.register('doctors', views.DoctorViewSet, basename='doctor')
router.register('patients', views.PatientViewSet, basename='patient')

doctor_router= routers.NestedDefaultRouter(router, 'doctors', lookup='doctor')
doctor_router.register('reviews', DoctorReviewViewSet, basename='doctor-review')



urlpatterns = [
    path('', include(router.urls)),
    path('', include(doctor_router.urls))
]
