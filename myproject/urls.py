"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, re_path
from myapp.views import main
import myapp.views
import newapp.views
import company.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('myapp/main', myapp.views.main),
    # path('myapp/about', myapp.views.about),
    # path('newapp/main', newapp.views.main),
    path('company/main', company.views.main),
    path('company/news', company.views.news),
    path('company/management', company.views.company_management),
    path('company/about', company.views.about),
    path('company/contacts', company.views.contacts),
    re_path('company/main', company.views.main),
    re_path('company/news', company.views.news),
    re_path('company/management', company.views.company_management),
    re_path('company/about', company.views.about),
    re_path('company/contacts', company.views.contacts),
    re_path(r'^company/news', company.views.news),

]
