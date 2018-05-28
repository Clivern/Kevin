"""
Context Module
"""

# local Django
from app.settings.info import *
from app.modules.util.helpers import Helpers
from app.modules.util.gravatar import Gravatar
from app.modules.entity.option_entity import Option_Entity
from app.modules.entity.user_entity import User_Entity

class Context():

    _data = {}
    _option_entity = Option_Entity()
    _user_entity = User_Entity()
    _helpers = Helpers()
    _logger = None


    def __init__(self):
        self._data["AUTHOR"] = AUTHOR
        self._data["COPYRIGHT"] = COPYRIGHT
        self._data["LICENSE"] = LICENSE
        self._data["VERSION"] = VERSION
        self._data["MAINTAINER"] = MAINTAINER
        self._data["EMAIL"] = EMAIL
        self._data["STATUS"] = STATUS
        self._data["REPO_URL"] = REPO_URL
        self._data["AUTHOR_URL"] = AUTHOR_URL
        self._data["RELEASES"] = RELEASES
        self._data["SUPPORT_URL"] = SUPPORT_URL
        self._logger = self._helpers.get_logger(__name__)


    def push(self, new_data):
        self._data.update(new_data)


    def load_options(self, options):
        options_to_load = {}
        for key in options.keys():
            options_to_load[key] = options[key]
            if not key in self._data.keys():
                self._data[key] = options[key]

        if len(options_to_load.keys()) > 0:
            new_options = self._option_entity.get_many_by_keys(options_to_load.keys())
            for option in new_options:
                self._data[option.key] = option.value


    def autoload_options(self):
        options = self._option_entity.get_many_by_autoload(True)
        for option in options:
            self._data[option.key] = option.value


    def autoload_user(self, user_id):
        user_data = {
            "user_first_name" : "",
            "user_last_name" : "",
            "user_username" : "",
            "user_email" : "",
            "user_avatar": ""
        }

        if user_id != None:
            user = self._user_entity.get_one_by_id(user_id)
            if user != False:
                user_data["user_first_name"] = user.first_name
                user_data["user_last_name"] = user.last_name
                user_data["user_username"] = user.username
                user_data["user_email"] = user.email
                user_data["user_avatar"] = Gravatar(user.email).get_image()

        self._data.update(user_data)


    def get(self, key = None, default = None):
        if key != None:
            return self._data[key] if key in self._data else default
        return self._data