"""
Profile Module
"""

# Django
from django.utils.translation import gettext as _
from django.contrib.auth import update_session_auth_hash

# local Django
from app.modules.util.token import Token
from app.modules.util.helpers import Helpers
from app.modules.util.gravatar import Gravatar
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


    def get_profile(self, user_id):

        profile_data = {
            "first_name" : "",
            "last_name" : "",
            "username" : "",
            "email" : "",
            "job_title" : "",
            "company" : "",
            "address" : "",
            "github_url" : "",
            "twitter_url" : "",
            "facebook_url" : "",
            "access_token": "",
            "refresh_token": "",
            "avatar": ""
        }

        user = self._user_entity.get_one_by_id(user_id)
        profile = self._profile_entity.get_profile_by_user_id(user_id)

        if user != False:
            profile_data["first_name"] = user.first_name
            profile_data["last_name"] = user.last_name
            profile_data["username"] = user.username
            profile_data["email"] = user.email
            profile_data["avatar"] = Gravatar(user.email).get_image()

        if profile != False:
            profile_data["job_title"] = profile.job_title
            profile_data["company"] = profile.company
            profile_data["address"] = profile.address
            profile_data["github_url"] = profile.github_url
            profile_data["twitter_url"] = profile.twitter_url
            profile_data["facebook_url"] = profile.facebook_url
            profile_data["access_token"] = profile.access_token
            profile_data["refresh_token"] = profile.refresh_token

        return profile_data


    def update_profile(self, user_id, user_data):
        user_data["user"] = user_id
        if self._profile_entity.profile_exists(user_data["user"]):
            status = self._profile_entity.update_profile(user_data)
            status &= self._user_entity.update_one_by_id(user_data["user"], user_data)
            return status
        else:
            status = (self._profile_entity.create_profile(user_data) != False)
            status &= self._user_entity.update_one_by_id(user_data["user"], user_data)
            return status


    def update_access_token(self, user_id):
        token = self._token.generate_token()
        while self._profile_entity.token_used(token) != False:
            token = self._token.generate_token()

        return token if self._profile_entity.update_access_token(user_id, token) else False


    def update_refresh_token(self, user_id):
        token = self._token.generate_token()
        while self._profile_entity.token_used(token) != False:
            token = self._token.generate_token()

        return token if self._profile_entity.update_refresh_token(user_id, token) else False


    def change_password(self, user_id, password):
        return self._user_entity.update_password_by_user_id(user_id, password)


    def restore_session(self, user_id, request):
        return update_session_auth_hash(request, self._user_entity.get_one_by_id(user_id))


    def validate_password(self, user_id, password):
        return self._user_entity.validate_password_by_user_id(user_id, password)


    def update_user(self, user_id, user_data):
        return self._user_entity.update_one_by_id(self, user_id, user_data)


    def username_used_elsewhere(self, user_id, username):
        user = self._user_entity.get_one_by_username(username)
        return False if user == False or user.id == user_id else True


    def email_used_elsewhere(self, user_id, email):
        user = self._user_entity.get_one_by_email(email)
        return False if user == False or user.id == user_id else True