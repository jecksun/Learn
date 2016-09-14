from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response


def home(request):
    return render(request, 'Site/home.html')


def about(request):
    return render_to_response('site/about.html')