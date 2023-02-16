from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.template.response import TemplateResponse


def index(request):
    return TemplateResponse(request, "books_app/index.html")

# def index(request):
#     template = loader.get_template('books_app/index.html')
#     return HttpResponse(template.render(), charset='utf-8')
# def index(request):
#     return render(request, "books_app/index.html")

def about(request):
    return HttpResponse("<h2>О сайте</h2>", charset='utf-8')


def contact(request):
    return HttpResponse("<h2>Контакты</h2>", charset='utf-8')


def products(request):
    return HttpResponse("<h2>Список товаров</h2>", charset='utf-8')


def top(request):
    return HttpResponse("<h2>Наиболее популярные товары</h2>", charset='utf-8')
