from django.urls import path

from .views import UserRegisterView,UserLoginView

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
]