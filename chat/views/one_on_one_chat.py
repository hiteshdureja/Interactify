from django.http import HttpResponseRedirect
from django.shortcuts import render

from chat.constants import ONE_ON_ONE_CHAT


def one_on_one_chat(request, **kwargs):
    recipient = kwargs.get("user_id")
    request.session["recipient"] = recipient
    user_id = request.session.get("user_id")
    if not user_id:
        return HttpResponseRedirect("/")
    return render(request, ONE_ON_ONE_CHAT, {"user_id": user_id})
