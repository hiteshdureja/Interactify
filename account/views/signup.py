from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from account.services import UserService


@csrf_exempt
def signup(request):
    request_get = request.GET
    first_name = request_get.get("first_name")
    last_name = request_get.get("last_name")
    dob = request_get.get("dob")
    email = request_get.get("email")
    password = request_get.get("password")
    confirm_password = request_get.get("confirm_password")

    if password != confirm_password:
        return render(
            "signup.html",
            {
                "errors": [
                    {
                        "field_name": "confirm_password",
                        "message": "Passwords do not match",
                    }
                ]
            },
        )

    # call create user from services
    user = UserService.create_user(
        first_name=first_name,
        last_name=last_name,
        dob=dob,
        email=email,
        password=password,
    )

    # redirect to otp validation screen
    return HttpResponseRedirect("/account/verify")
