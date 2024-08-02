from django.urls import path
from .views import ChangePasswordView, CustomLoginView, CustomRegisterView, activate, login_view, logout_view, register_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('confirmation/<str:uidb64>/<str:token>/', activate, name='confirmation'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
]
