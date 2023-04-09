from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from account.services import UserService


@csrf_exempt
def signup(request):
    request_post = request.POST
    user_id = request_post.get("user_id")
    first_name = request.GET.get("first_name")
    last_name = request_post.get("last_name")
    dob = request_post.get("dob")
    email = request_post.get("email")
    password = request_post.get("password")
    confirm_password = request_post.get("confirm_password")

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
    UserService.create_user(
        user_id=user_id,
        first_name=first_name,
        last_name=last_name,
        dob=dob,
        email=email,
        password=password,
    )

    # redirect to otp validation screen
    return HttpResponseRedirect("/account/verify")
