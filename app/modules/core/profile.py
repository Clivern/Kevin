"""
Profile Module
"""

# Django
from django.contrib.auth import authenticate, login
from django.core.validators import validate_email

# local Django
from app.modules.util.helpers import Helpers
from app.modules.entity.option_entity import Option_Entity
from app.modules.entity.user_entity import User_Entity


class Profile():

    _option_entity = None
    _user_entity = None
    _helpers = None
    _logger = None


    def __init__(self):
        self._option_entity = Option_Entity()
        self._user_entity = User_Entity()
        self._helpers = Helpers()
        self._logger = self._helpers.get_logger(__name__)


    def update_profile(self, user_data):

        pass

    def profile_exists(self, user_id):
        pass
