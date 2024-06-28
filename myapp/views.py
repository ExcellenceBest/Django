from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return HttpResponse(
        """<h1>Добро пожаловать на главную страницу</h1>"""
    )

def about(recuest):
    return HttpResponse(
        """<h1>Добро пожаловать страницу о нас</h1>"""
    )
