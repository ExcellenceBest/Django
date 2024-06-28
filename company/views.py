from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return HttpResponse(
        """
        <h1 style="background-color: red">Добро пожаловать на главную страницу компании!</h1>
        """)


def news(request):
    return HttpResponse(
        """<h1 style="background-color:blue">Новости компании!</h1>
                """)


def company_management(request):
    return HttpResponse(
        """<h1 style="background-color:green">Руководство компании!</h1>
                        """)


def about(request):
    return HttpResponse(
        """<h1 style="background-color:grey">O компании!</h1>
                        """)


def contacts(request):
    return HttpResponse(
        """<h1 style="background-color:yellow">Контакты компании!</h1>
                        """)
