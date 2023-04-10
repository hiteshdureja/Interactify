from django.shortcuts import render

from chat.constants import ONE_ON_ONE_CHAT


def one_on_one_chat(request):
    return render(request, ONE_ON_ONE_CHAT, {})
