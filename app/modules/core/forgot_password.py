"""
Forgot Password Module
"""

from app.modules.util.helpers import Helpers
from app.modules.entity.user_entity import User_Entity
from app.modules.entity.option_entity import Option_Entity
from app.modules.entity.reset_request_entity import Reset_Request

class Forgot_Password():

    _reset_request = None
    _option_entity = None
    _helpers = None

    def __init__(self):
        self._reset_request = Reset_Request()
        self._option_entity = Option_Entity()
        self._helpers = Helpers()


    def check_email(self, email):
        pass

    def is_spam(self, email):
        pass

    def create_token(self, email):
        pass

    def send_message(self, email, token):
        pass