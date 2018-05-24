"""
Profile Module
"""

# Django
from django.utils.translation import gettext as _

# local Django
from app.modules.util.token import Token
from app.modules.util.helpers import Helpers
from app.modules.entity.profile_entity import Profile_Entity
from app.modules.entity.option_entity import Option_Entity
from app.modules.entity.user_entity import User_Entity


class Profile():

    _option_entity = Option_Entity()
    _user_entity = User_Entity()
    _helpers = Helpers()
    _logger = None
    _token = Token()
    _profile_entity = Profile_Entity()


    def __init__(self):
        self._logger = self._helpers.get_logger(__name__)


    def update_profile(self, user_id, user_data):
        user_data["user"] = user_id
        if self._profile_entity.profile_exists(user_data["user"]):
            return self._profile_entity.update_profile(user_data)
        else:
            return self._profile_entity.create_profile(user_data)


    def update_access_token(self, user_id):
        token = self._token.generate_token()
        while self._token.token_used(toke) != False:
            token = self._token.generate_token()

        return token if self._profile_entity.update_access_token(self, user_id, token) else False


    def update_refresh_token(self, user_id):
        token = self._token.generate_token()
        while self._token.token_used(toke) != False:
            token = self._token.generate_token()

        return token if self._profile_entity.update_refresh_token(self, user_id, token) else False


    def change_password(self, user_id, password):
        return self._user_entity.update_password_by_user_id(user_id, password)


    def update_user(self, user_id, user_data):
        return self._user_entity.update_one_by_id(self, user_id, user_data)


    def username_used_elsewhere(self, user_id, username):
        user = self._user_entity.get_one_by_username(username)
        return False if user == False or user.id == user_id else True


    def email_used_elsewhere(self, user_id, email):
        user = self._user_entity.get_one_by_email(email)
        return False if user == False or user.id == user_id else True