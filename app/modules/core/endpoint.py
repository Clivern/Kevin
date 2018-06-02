"""
Endpoint Module
"""

# local Django
from app.modules.util.helpers import Helpers
from app.modules.entity.namespace_entity import Namespace_Entity
from app.modules.entity.endpoint_entity import Endpoint_Entity


class Endpoint():

    __helpers = Helpers()
    __logger = None
    __namespace_entity = Namespace_Entity()
    __endpoint_entity = Endpoint_Entity()