"""
Context Module
"""

# local Django
from app.settings.info import *


class Context():

    _data = {}


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


    def push(self, new_data):
        self._data.update(new_data)


    def get(self):
        return self._data