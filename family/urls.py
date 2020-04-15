from django.urls import path, include
from . import api

urlpatterns = [
    path('get', api.get)
]
