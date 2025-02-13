from django.urls import path
from .views import UserRegistrationView, UserLoginView, PatientListCreateView, HeartRateListCreateView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('patients_create/', PatientListCreateView.as_view(), name='create_patients'),
     path('patients_list/', PatientListCreateView.as_view(), name='list_patients'),
    path('heart_rate_create/', HeartRateListCreateView.as_view(), name='create_heart-rate'),
    path('heart_rate_list/', HeartRateListCreateView.as_view(), name='list_heart-rate'),
]
