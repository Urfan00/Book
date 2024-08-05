from django.urls import path
from .views import ChangePasswordView, CustomLoginView, CustomRegisterView, ResetPasswordConfirmView, ResetPasswordView, activate, login_view, logout_view, register_view
from django.contrib.auth.views import PasswordResetCompleteView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),

    path('register/', CustomRegisterView.as_view(), name='register'),
    path('confirmation/<str:uidb64>/<str:token>/', activate, name='confirmation'),

    path('change_password/', ChangePasswordView.as_view(), name='change_password'),

    path('reset_password/', ResetPasswordView.as_view(), name='reset_password'),
    path('reset_password_confirm/<str:uidb64>/<str:token>/', ResetPasswordConfirmView.as_view(), name='reset_password_confirm'),
    path('reset_password_complete/', PasswordResetCompleteView.as_view(template_name='accounts/reset_password_complete.html'),name='reset_password_complete'),
]
