from django.urls import path
from account.views import index, otp_verification, logout

urlpatterns = [
    path("", index),
    path("logout/", logout),
    path("otp/verify", otp_verification),
]
