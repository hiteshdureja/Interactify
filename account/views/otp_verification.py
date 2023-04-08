from django.http import HttpResponseRedirect
from django.shortcuts import render

from account.services import UserService


def otp_verification(request):
    request_post = request.POST
    otp = request_post.get("otp")
    user_id = request_post.get("user_id")
    validated = UserService.validate_otp(user_id=user_id, otp=otp)
    if not validated:
        return render(
            "otp_verification.html",
            {
                "errors": [
                    {
                        "field_name": "otp",
                        "message": "Incorrect OTP",
                    }
                ]
            },
        )

    return HttpResponseRedirect("/account/dashboard")
