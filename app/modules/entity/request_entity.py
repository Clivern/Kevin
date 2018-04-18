"""
Request Entity Module
"""

from app.models import Endpoint
from app.models import Request
from app.models import Request_Meta
from django.contrib.auth.models import User
from app.modules.util.helpers import Helpers

class Request_Entity():

    GET = "get"
    POST = "post"
    HEADE = "head"
    PUT = "put"
    DELETE = "delete"
    PATCH = "patch"
    TRACE = "trace"
    OPTIONS = "options"
    CONNECT = "connect"
    VALID = "valid"
    NOT_VALID = "not_valid"
    DEBUG = "debug"


    def insert_one(self, request):
        """Insert a New Request"""
        request = Request(
            uri=request["uri"],
            method=request["method"],
            headers=request["headers"],
            body=request["body"],
            status=request["status"],
            endpoint=Endpoint.objects.get(pk=request["endpoint_id"])
        )

        request.save()
        return False if request.pk is None else request


    def insert_many(self, requests):
        """Insert Many Requests"""
        status = True
        for request in requests:
            status &= True if self.insert_one(request) != False else False
        return status


    def get_one_by_id(self, id):
        """Get Request By ID"""
        try:
            request = Request.objects.get(pk=id)
            return False if request.pk is None else request
        except:
            return False


    def get_many_by_requests(self, endpoint_id):
        """Get Many Requests By Endpoint ID"""
        requests = Request.objects.filter(endpoint=endpoint_id)
        return requests


    def update_one_by_id(self, id, new_data):
        """Update Request By ID"""
        request = self.get_one_by_id(id)
        if request != False:
            if "uri" in new_data:
                request.uri = new_data["uri"]

            if "method" in new_data:
                request.method = new_data["method"]

            if "headers" in new_data:
                request.headers = new_data["headers"]

            if "body" in new_data:
                request.body = new_data["body"]

            if "status" in new_data:
                request.status = new_data["status"]

            if "namespace_id" in new_data:
                request.endpoint = Endpoint.objects.get(pk=new_data["endpoint_id"])

            request.save()
            return True
        return False


    def delete_one_by_id(self, id):
        """Delete Request By ID"""
        request = self.get_one_by_id(id)
        if request != False:
            count, deleted = request.delete()
            return True if count > 0 else False
        return False