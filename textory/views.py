from django.shortcuts import redirect
from django.http import HttpResponse


def login_redirect(request):
    return redirect('/story')
