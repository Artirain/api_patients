from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import PatientListView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('patients/', PatientListView.as_view(), name='patients'),
]
