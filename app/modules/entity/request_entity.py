"""
Request Entity Module
"""

# Django
from django.contrib.auth.models import User

# local Django
from app.models import Endpoint
from app.models import Request
from app.models import Request_Meta
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


    def get_many_by_endpoint(self, endpoint_id):
        """Get Many Requests By Endpoint ID"""
        requests = Request.objects.filter(endpoint=endpoint_id)
        return requests


    def count_by_endpoint_date(self, limit, endpoint_ids = []):
        if len(endpoint_ids) <= 0:
            return []
        return Request.objects.raw("select count(id) as id, DATE(created_at) as count_date from app_request where endpoint_id in (%s) group by count_date order by count_date desc limit %s;" % (",".join(str(x) for x in endpoint_ids), limit))


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

            if "endpoint_id" in new_data:
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