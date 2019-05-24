from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'invitation/home.html')


def profile(request):
    return render(request, 'invitation/profile.html')