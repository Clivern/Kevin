"""
Install Module
"""

# Django
from django.core.management import execute_from_command_line

# local Django
from app.modules.util.helpers import Helpers
from app.modules.entity.option_entity import Option_Entity
from app.modules.entity.user_entity import User_Entity


class Install():

    _option_entity = None
    _user_entity = None
    _options = [
        {"key": "app_installed", "value": "true", "autoload": True},
        {"key": "reset_mails_messages_count", "value": "5", "autoload": False},
        {"key": "reset_mails_expire_after", "value": "24", "autoload": False},
        {"key": "google_analytics_account", "value": "", "autoload": True}
    ]
    _admin = {
        "username" : "",
        "email" : "",
        "password" : "",
        "is_superuser": True,
        "is_active": True,
        "is_staff": False
    }
    _helpers = None
    _logger = None


    def __init__(self):
        self._option_entity = Option_Entity()
        self._user_entity = User_Entity()
        self._helpers = Helpers()
        self._logger = self._helpers.get_logger(__name__)


    def is_installed(self):
        return False if self._option_entity.get_one_by_key("app_installed") == False else True


    def set_app_data(self, name, email, url):
        self._options.append({"key": "app_name", "value": name, "autoload": True})
        self._options.append({"key": "app_email", "value": email, "autoload": True})
        self._options.append({"key": "app_url", "value": url, "autoload": True})


    def set_admin_data(self, username, email, password):
        self._admin["username"] = username
        self._admin["email"] = email
        self._admin["password"] = password


    def install(self):
        try:
            execute_from_command_line(["manage.py", "migrate"])
        except Exception as e:
            self._logger.error("Error While Running Migrations: %s" % e)
            return False

        status = True
        status &= self._option_entity.insert_many(self._options)
        status &= (self._user_entity.insert_one(self._admin) != False)
        return status