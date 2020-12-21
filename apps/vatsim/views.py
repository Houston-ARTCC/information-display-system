import os
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import redirect

from apps.vatsim.connect import process_oauth


def auth(request):
    if 'code' not in request.GET:
        return redirect('https://auth.vatsim.net/oauth/authorize'
                        '?client_id=' + os.getenv('VATSIM_CONNECT_CLIENT_ID') +
                        '&redirect_uri=' + os.getenv('VATSIM_CONNECT_REDIRECT_URI') +
                        '&response_type=code'
                        '&scope=full_name+vatsim_details+email')

    user = process_oauth(request.GET.get('code'))

    if user is None:
        return HttpResponse(status=500)

    login(request, user)
    return redirect('home')


def deauth(request):
    logout(request)
    return redirect('home')
