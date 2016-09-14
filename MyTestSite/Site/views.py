from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from Site.models import Articles


def home(request):
    articles = Articles.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'Site/home.html', context)


def about(request):
    return render(request, 'Site/about.html')