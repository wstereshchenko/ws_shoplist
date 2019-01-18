from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import shop_list


urlpatterns = [
    url(r'$', shop_list)
]
