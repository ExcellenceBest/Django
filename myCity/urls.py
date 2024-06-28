from django.contrib import admin
from django.urls import path, re_path

import myCity.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mycity', myCity.views.mycity),
    path('mycity/news', myCity.views.news),
    re_path(r'mycity/news', myCity.views.news),
    path('mycity/management', myCity.views.management),
    re_path('mycity/management', myCity.views.management),
    path('mycity/facts', myCity.views.facts),
    re_path('mycity/facts', myCity.views.facts),
    path('mycity/contacts', myCity.views.contacts),
    re_path('mycity/contacts', myCity.views.contacts),
]

