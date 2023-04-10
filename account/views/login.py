from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from account.services import UserService


@csrf_exempt
def login(request):
    request_post = request.POST
    user_id = request_post.get("user_id")
    password = request_post.get("password")

    if not user_id or not password:
        return render(request, "account.html", {})

    user_logged_in = UserService.login_user(
        user_id=user_id,
        password=password,
    )
    if not user_logged_in:
        return render(
            "login.html",
            {
                "errors": [
                    {
                        "field_name": "password",
                        "message": "Incorrect username or password",
                    }
                ]
            },
        )

    return HttpResponseRedirect("/account/dashboard")
