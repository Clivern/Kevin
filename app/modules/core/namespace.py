"""
Namespace Module
"""

# local Django
from app.modules.util.helpers import Helpers
from app.modules.entity.namespace_entity import Namespace_Entity
from app.modules.entity.endpoint_entity import Endpoint_Entity


class Namespace():

    __helpers = Helpers()
    __logger = None
    __namespace_entity = Namespace_Entity()
    __endpoint_entity = Endpoint_Entity()


    def __init__(self):
        self.__logger = self.__helpers.get_logger(__name__)


    def user_owns(self, namespace_id, user_id):
        return self.__namespace_entity.user_owns(namespace_id, user_id)


    def delete_namespace(self, namespace_id):
        return self.__namespace_entity.delete_one_by_id(namespace_id)


    def slug_used(self, slug):
        return (self.__namespace_entity.get_one_by_slug(slug) != False)


    def slug_used_elsewhere(self, namespace_id, slug):
        namespace = self.__namespace_entity.get_one_by_slug(slug)
        return False if namespace == False or namespace.id == namespace_id else True


    def insert_one(self, namespace):
        return self.__namespace_entity.insert_one(namespace)


    def update_one_by_id(self, namespace_id, new_data):
        return self.__namespace_entity.update_one_by_id(namespace_id, new_data)


    def get_one_by_slug(self, slug):
        return self.__namespace_entity.get_one_by_slug(slug)


    def get_many_by_user(self, user_id):
        namespaces = self.__namespace_entity.get_many_by_user(user_id)
        for namespace in namespaces:
            namespace.endpoints_count = self.__endpoint_entity.count_by_namespace(namespace.id)
        return namespaces