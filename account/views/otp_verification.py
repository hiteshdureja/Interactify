from django.http import HttpResponseRedirect
from django.shortcuts import render
from account.constants import TEMPLATE_OTP_VERIFICATION

from account.services import UserCredentialService


def otp_verification(request):
    request_post = request.POST
    if not len(request_post):
        return render(request, TEMPLATE_OTP_VERIFICATION, {})
    otp = request_post.get("otp")
    user_id = request_post.get("user_id")
    validated = UserCredentialService.validate_otp(user_id=user_id, otp=otp)
    if not validated:
        return render(
            request,
            TEMPLATE_OTP_VERIFICATION,
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
