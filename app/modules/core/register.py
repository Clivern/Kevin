"""
Register Module
"""

from app.modules.util.helpers import Helpers
from app.modules.entity.option_entity import Option_Entity
from app.modules.entity.user_entity import User_Entity

class Register():

    _option_entity = None
    _user_entity = None
    _helpers = None
    _logger = None

    def __init__(self):
        self._option_entity = Option_Entity()
        self._user_entity = User_Entity()
        self._helpers = Helpers()
        self._logger = self._helpers.get_logger(__name__)

    def username_used(self, username):
        return False if self._user_entity.get_one_by_username(username) == False else True

    def email_used(self, email):
        return False if self._user_entity.get_one_by_email(email) == False else True

    def create_user(self, user_data):
        status = True
        status &= (self._user_entity.insert_one({
            "username" : user_data["username"],
            "email" : user_data["email"],
            "password" : user_data["password"],
            "first_name" : user_data["first_name"],
            "last_name" : user_data["last_name"],
            "is_superuser": False,
            "is_active": True,
            "is_staff": False
        }) != False)

        return status