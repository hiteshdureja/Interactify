from django.urls import path

from account.views.signup import signup

urlpatterns = [
    path("signup", signup),
]
