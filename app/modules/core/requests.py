"""
Request Module
"""
# standard library
import json

# local Django
from app.modules.util.helpers import Helpers
from app.modules.entity.namespace_entity import Namespace_Entity
from app.modules.entity.endpoint_entity import Endpoint_Entity
from app.modules.entity.request_entity import Request_Entity


class Request():

    __helpers = Helpers()
    __logger = None
    __namespace_entity = Namespace_Entity()
    __endpoint_entity = Endpoint_Entity()
    __request_entity = Request_Entity()


    def __init__(self):
        self.__logger = self.__helpers.get_logger(__name__)


    def insert_one(self, request):
        return self.__request_entity.insert_one(request)


    def user_owns(self, request_id, user_id):
        return self.__request_entity.user_owns(request_id, user_id)


    def delete_request(self, request_id):
        return self.__request_entity.delete_one_by_id(request_id)


    def get_many_by_endpoint(self, endpoint_id, order_by, asc):
        requests = self.__request_entity.get_many_by_endpoint(endpoint_id, order_by, asc)
        for request in requests:
            data = []
            try:
                data = json.loads(request.headers)
            except Exception as e:
                self.delete_request(request.id)

            request.headers = data
            request.body = json.loads(request.body)
            request.body = json.dumps(request.body, indent=4)

        return requests