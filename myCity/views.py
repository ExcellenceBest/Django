from django.shortcuts import render
from django.http import HttpResponse
from myCity import urls


def mycity(request):
    return HttpResponse(
        """<h1>Добро пожаловать на портал нашего города!!!</h1>""")


def news(request):
    return HttpResponse(
        """<h1>Новости нашего города!!!</h1>""")


def management(request):
    return HttpResponse(
        """<h1>Руководство нашего города!!!</h1>""")


def facts(request):
    return HttpResponse(
        """<h1>Факты о городе</h1>""")


def contacts(request):
    return HttpResponse(
        """<h1>Контакты</h1>""")
