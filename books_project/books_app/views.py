from django.http import HttpResponse


def index(request):
    return HttpResponse("<h2>Главная страница</h2>", charset='utf-8')


def about(request):
    return HttpResponse("<h2>О сайте</h2>", charset='utf-8')


def contact(request):
    return HttpResponse("<h2>Контакты</h2>", charset='utf-8')


def products(request):
    return HttpResponse("<h2>Список товаров</h2>", charset='utf-8')


def top(request):
    return HttpResponse("<h2>Наиболее популярные товары</h2>", charset='utf-8')
