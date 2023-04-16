from django.http import HttpResponseRedirect


def logout(request):
    del request.session["user_id"]
    return HttpResponseRedirect("/")
