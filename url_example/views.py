from django.shortcuts import render
from django.http import HttpResponse

def profile(request, username='Default user'):

    return HttpResponse('<h1>This is the profile page!, and the user is {}.</h1>'.format(username))
