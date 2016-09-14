from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
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


def show_article(request, article_id):
    article = get_object_or_404(Articles, id = article_id)
    return render(request, 'Site/article.html', {'article':article})
