from django.http import HttpResponseRedirect
from django.shortcuts import render
from account.constants import TEMPLATE_OTP_VERIFICATION

from account.services import UserCredentialService


def otp_verification(request):
    request_post = request.POST
    if not len(request_post):
        return render(request, TEMPLATE_OTP_VERIFICATION, {})
    otp = request_post.get("otp")
    user_id = request.session["user_id"]
    user_credential_service = UserCredentialService()
    if not user_credential_service.validate_otp(user_id=user_id, otp=otp):
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

    request.session["user_id"] = user_id
    return HttpResponseRedirect("/feed/")
