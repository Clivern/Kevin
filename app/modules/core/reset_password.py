"""
Reset Password Module
"""

from django.utils import timezone
from datetime import timedelta
from app.modules.util.helpers import Helpers
from app.modules.entity.user_entity import User_Entity
from app.modules.entity.reset_request_entity import Reset_Request_Entity

class Reset_Password():

    _reset_request_entity = None
    _helpers = None
    _user_entity = None


    def __init__(self):
        self._helpers = Helpers()
        self._user_entity = User_Entity()
        self._reset_request_entity = Reset_Request_Entity()


    def check_token(self, token):
        request = self._reset_request_entity.get_one_by_token(token)
        if request != False and timezone.now() < request.expire_at:
            return True
        return False


    def reset_password(self, email, token, new_password):
        request = self._reset_request_entity.get_one_by_token(token)
        if request != False and timezone.now() < request.expire_at and request.email == email:
            return self._user_entity.update_password_by_email(self, email, new_password);
        return False


    def delete_reset_request(self, token):
        return self._reset_request_entity.delete_one_by_token(token)