from django.shortcuts import render
from .models import *


def index(request):
    news = News.objects.all()
    context = {
        'news' : news
    }

    return render(request, template_name='blog/index.html', context=context)