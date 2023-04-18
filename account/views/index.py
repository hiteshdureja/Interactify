from django.http import HttpResponseRedirect
from django.shortcuts import render
from account.services import UserService


def index(request):
    user_id = request.session.get("user_id")
    if user_id:
        return HttpResponseRedirect("/feed/")
    request_post = request.POST
    if not request_post:
        return render(request, "index.html", {"user_logged_in": False})

    user_id = request_post.get("user_id")
    email = request_post.get("email")
    first_name = request_post.get("first_name")
    last_name = request_post.get("last_name")
    password = request_post.get("password")
    confirm_password = request_post.get("confirm_password")

    user_login = request_post.get("user_login")
    password_login = request_post.get("password_login")

    if user_login and password_login:
        user_logged_in = UserService.login_user(
            user_id=user_login,
            password=password_login,
        )

        if not user_logged_in:
            return render(
                request,
                "index.html",
                {
                    "errors": [
                        {
                            "field_name": "password_login",
                            "message": "Incorrect username or password",
                        }
                    ]
                },
            )
        request.session["user_id"] = user_login
        return HttpResponseRedirect("/feed/")

    if password != confirm_password:
        return render(
            request,
            "index.html",
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
        email=email,
        password=password,
    )
    # redirect to otp validation screen
    return HttpResponseRedirect("/otp/verify")
