"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from http.client import responses

from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request
from django.urls import path
from django.http import Http404


def index(request):
    return HttpResponse('<h1>hello</h1>')

def book_list(request):
    # book_text = ''
    #
    # for i in range(0, 10):
    #     book_text += f'book {i}<br>'

    return render(request, template_name= 'book_list.html', context={'range':range(0, 10)})

def book(request, num):
    return render(request, template_name="book_detail.html", context={'num': num})

bike_list = [
    {'title': 'YAMAHA', 'Best_Bike': 'YZF-R1M'},
    {'title': 'HONDA', 'Best_Bike': 'CBR1000RR-R_Fire_Blade'},
    {'title': 'KAWASAKI', 'Best_Bike': 'H2R'},
    {'title': 'BMW', 'Best_Bike': 'BMW_S1000RR-M-Package'},
    {'title': 'DUKATI', 'Best_Bike': 'Oanigale_V4-SP'},

]
#
# bike_name = yamaha = ['YZF_R1', 'YZF_R9', 'YZF_R7', 'YZF_R6'],
# honda = ['CBR1000rr', 'CBR650R', 'CBR600RR', 'CBR300RR'],
# kawasaki = ['H2', '10R', '6R', 'ninja650']
#
# def bike_list(request, name, bike_name):
#     bike_text = f'{name}의 대표적인 바이크{bike_name}입니다.'
#     return HttpResponse(bike_text)

def language(request, lang):
    return HttpResponse(f'<h1>{lang} 언어 페이지입니다.</h1>')

def bikes(request):
    # bike_titles = [bike['title'] for bike in bike_list]
    #
    # response_text = ''
    #
    # for index, title in enumerate(bike_titles):
    #     response_text += f'<a href="/bike/{index}/">{title}</a><br>'
    #
    # return HttpResponse(response_text)

    return render(request, template_name= 'bike.html', context= {'bike_list': bike_list})

def bike_detail(request, index):
    if index > len(bike_list) -1:
        raise Http404

    bike = bike_list[index]

    return render(request, template_name='bikes.html', context={'bike': bike})
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('book_list/', book_list),
    path('language/<str:lang>', language),
    path('book_list/<int:num>/', book),
    # path('bike_list/<str:name>', bike_list),
    path('bike/', bikes),
    path('bike/<int:index>/', bike_detail),
]
