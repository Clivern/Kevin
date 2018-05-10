"""
Login Module
"""

# Django
from django.contrib.auth import authenticate, login
from django.core.validators import validate_email

# local Django
from app.modules.util.helpers import Helpers
from app.modules.entity.option_entity import Option_Entity
from app.modules.entity.user_entity import User_Entity


class Login():

    _option_entity = None
    _user_entity = None
    _helpers = None
    _logger = None


    def __init__(self):
        self._option_entity = Option_Entity()
        self._user_entity = User_Entity()
        self._helpers = Helpers()
        self._logger = self._helpers.get_logger(__name__)


    def is_authenticated(self, request):
        if request.user and request.user.is_authenticated:
            return True
        else:
            return False


    def authenticate(self, username_email, password, request=None, with_login = True):
        is_email = False
        try:
            is_email = True if validate_email(username_email) == None else False
        except Exception as e:
            is_email = False
        if is_email:
            user = self._user_entity.get_one_by_email(username_email)
            if user != False and user.check_password(password) == True:
                if with_login:
                    self.login(request, user)
                return True
            else:
                return False
        else:
            user = authenticate(request=request, username=username_email, password=password)
            if user is not None:
                if with_login:
                    self.login(request, user)
                return True
            else:
                return False


    def login(self, request, user):
        return login(request, user)