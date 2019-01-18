from django.conf.urls import url
from .views import user_login, user_logout, register

urlpatterns = [
    url(r'login', user_login, name='login'),
    url(r'logout', user_logout, name='logout'),
    url(r'register', register, name='register'),
]
