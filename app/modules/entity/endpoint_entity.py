"""
Endpoint Entity Module
"""

# Django
from django.contrib.auth.models import User

# local Django
from app.models import Endpoint
from app.models import Namespace
from app.models import Endpoint_Meta
from app.modules.util.helpers import Helpers


class Endpoint_Entity():

    GET = "get"
    POST = "post"
    HEADE = "head"
    PUT = "put"
    DELETE = "delete"
    PATCH = "patch"
    TRACE = "trace"
    OPTIONS = "options"
    CONNECT = "connect"
    ANY = "any"
    VALIDATE = "validate"
    DEBUG = "debug"
    DYNAMIC = "dynamic"


    def insert_one(self, endpoint):
        """Insert a New Endpoint"""
        endpoint = Endpoint(
            route=endpoint["route"],
            method=endpoint["method"],
            target=endpoint["target"],
            route_rules=endpoint["route_rules"],
            headers_rules=endpoint["headers_rules"],
            body_rules=endpoint["body_rules"],
            namespace=Namespace.objects.get(pk=endpoint["namespace_id"])
        )
        endpoint.save()
        return False if endpoint.pk is None else endpoint


    def insert_many(self, endpoints):
        """Insert Many Endpoints"""
        status = True
        for endpoint in endpoints:
            status &= True if self.insert_one(endpoint) != False else False
        return status


    def get_one_by_id(self, id):
        """Get Endpoint By ID"""
        try:
            endpoint = Endpoint.objects.get(pk=id)
            return False if endpoint.pk is None else endpoint
        except:
            return False


    def get_many_by_namespace(self, namespace_id, order_by, asc):
        """Get Many Endpoints By Namespace ID"""
        endpoints = Endpoint.objects.filter(namespace=namespace_id).order_by(order_by if asc else "-%s" % order_by)
        return endpoints


    def get_many_ids_by_namespace(self, namespace_id):
        """Get Many Endpoints By Namespace ID"""
        endpoints = Endpoint.objects.filter(namespace=namespace_id)
        return [endpoint.id for endpoint in endpoints]


    def count_by_namespace(self, namespace_id):
        """Count Endpoints By Namespace ID"""
        count = Endpoint.objects.filter(namespace=namespace_id).count()
        return count


    def count_by_target(self, target, namespace_id):
        count = Endpoint.objects.filter(namespace=namespace_id, target=target).count()
        return count


    def update_one_by_id(self, id, new_data):
        """Update Endpoint By ID"""
        endpoint = self.get_one_by_id(id)
        if endpoint != False:
            if "route" in new_data:
                endpoint.route = new_data["route"]

            if "method" in new_data:
                endpoint.method = new_data["method"]

            if "target" in new_data:
                endpoint.target = new_data["target"]

            if "route_rules" in new_data:
                endpoint.route_rules = new_data["route_rules"]

            if "headers_rules" in new_data:
                endpoint.headers_rules = new_data["headers_rules"]

            if "body_rules" in new_data:
                endpoint.body_rules = new_data["body_rules"]

            if "namespace_id" in new_data:
                endpoint.namespace = Namespace.objects.get(pk=new_data["namespace_id"])

            endpoint.save()
            return True
        return False


    def delete_one_by_id(self, id):
        """Delete Endpoint By ID"""
        endpoint = self.get_one_by_id(id)
        if endpoint != False:
            count, deleted = endpoint.delete()
            return True if count > 0 else False
        return False