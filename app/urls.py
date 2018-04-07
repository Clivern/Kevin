"""
Routes File For Kevin
"""

from django.contrib import admin
from django.urls import path
from app.controllers.web.home import Home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', Home.index, name='home')
]
