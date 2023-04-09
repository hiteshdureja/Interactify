from django.urls import path

from account.views import signup, login, otp_verification

urlpatterns = [
    path("signup", signup),
    path("login", login),
    path("otp/verify", otp_verification),
]
