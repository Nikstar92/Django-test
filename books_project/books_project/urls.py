"""books_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from books_app import views

product_patterns = [
    path("", views.products, name="products_list"),
    path("top", views.top, name='products_top'),

]

about_patterns = [
    path("", views.about, name="about"),
    path("contacts/", views.contacts, name="about_contacts"),
]

urlpatterns = [
    path("about/", include(about_patterns)),
    path("products/", include(product_patterns)),
    path('index/', views.index, name="index"),
    path('admin/', admin.site.urls),
]
