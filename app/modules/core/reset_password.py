"""
Reset Password Module
"""

from app.modules.util.helpers import Helpers
from app.modules.entity.user_entity import User_Entity
from app.modules.entity.option_entity import Option_Entity
from app.modules.entity.reset_request_entity import Reset_Request

class Reset_Password():

    _reset_request = None
    _option_entity = None
    _helpers = None
    _user_entity = None

    def __init__(self):
        self._reset_request = Reset_Request()
        self._option_entity = Option_Entity()
        self._helpers = Helpers()
        self._user_entity = User_Entity()

    def check_token(self, token):
        pass

    def reset_password(self, email, token, new_password):
        pass

    def delete_reset_request(self, email, token):
        pass