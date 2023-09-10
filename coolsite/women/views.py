from django.http import HttpResponse
from django.shortcuts import render
from .models import *

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'addpage'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}
]


def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная'
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'title': 'Описание'})


def addpage(request):
    return HttpResponse('addpage')


def contact(request):
    return HttpResponse('contact')


def login(request):
    return HttpResponse('login')


def show_post(request, post_id):
    return HttpResponse(f'post {post_id}')
