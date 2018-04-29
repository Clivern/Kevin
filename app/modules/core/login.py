"""
Login Module
"""

from django.contrib.auth import authenticate
from app.modules.entity.option_entity import Option_Entity
from app.modules.entity.user_entity import User_Entity

class Login():

    _option_entity = None
    _user_entity = None

    def __init__(self):
        self._option_entity = Option_Entity()
        self._user_entity = User_Entity()

    def is_authenticated(self, request):
        if request.user and request.user.is_authenticated:
            return True
        else:
            return False

    def authenticate(self, username, password, request=None):
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            return True
        else:
            return False