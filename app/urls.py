"""
Routes For Kevin
"""

from django.contrib import admin
from django.urls import path
from app.controllers.web.home import Home


urlpatterns = [
    path('', Home.as_view(), name='home')
]
