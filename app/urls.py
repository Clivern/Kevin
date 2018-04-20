"""
Routes For Kevin
"""

from django.contrib import admin
from django.urls import path
from app.controllers.web.dashboard import Dashboard
from app.controllers.web.endpoint import Endpoint
from app.controllers.web.endpoints import Endpoints
from app.controllers.web.forgot_password import ForgotPassword
from app.controllers.web.home import Home
from app.controllers.web.login import Login
from app.controllers.web.profile import Profile
from app.controllers.web.not_found import NotFound
from app.controllers.web.error import Error
from app.controllers.web.install import Install


urlpatterns = [
    path('', Home.as_view(), name='web.home'),
    path('install', Install.as_view(), name='web.install'),
    path('dashboard', Dashboard.as_view(), name='web.dashboard'),
    path('endpoint/<slug:endpoint>', Endpoint.as_view(), name='web.endpoint'),
    path('endpoints', Endpoints.as_view(), name='web.endpoints'),
    path('forgot_password', ForgotPassword.as_view(), name='web.forgot_password'),
    path('login', Login.as_view(), name='web.login'),
    path('profile', Profile.as_view(), name='web.profile'),
    path('404', NotFound.as_view(), name='web.not_found'),
    path('500', Error.as_view(), name='web.error')
]
