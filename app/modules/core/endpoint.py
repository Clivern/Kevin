"""
Endpoint Module
"""

# local Django
from app.modules.util.helpers import Helpers
from app.modules.entity.namespace_entity import Namespace_Entity
from app.modules.entity.endpoint_entity import Endpoint_Entity
from app.modules.entity.request_entity import Request_Entity


class Endpoint():

    __helpers = Helpers()
    __logger = None
    __namespace_entity = Namespace_Entity()
    __endpoint_entity = Endpoint_Entity()
    __request_entity = Request_Entity()


    def get_one_by_id(self, endpoint_id):
        return self.__endpoint_entity.get_one_by_id(endpoint_id)


    def count_by_target(self, target, namespace_id):
        return self.__endpoint_entity.count_by_target(target, namespace_id)


    def get_many_by_namespace_id(self, namespace_id):
        endpoints  = self.__endpoint_entity.get_many_by_namespace(namespace_id)
        for endpoint in endpoints:
            if endpoint.target == 'validate':
                endpoint.status = self.__request_entity.get_latest_status(endpoint.id)
            elif endpoint.target == 'dynamic':
                endpoint.status = "dynamic"
            else:
                endpoint.status = "debug"
        return endpoints