"""
Request Module
"""
# standard library
import json
import re

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
            if request.body != '':
                try:
                    request.body = json.loads(request.body)
                    request.body = json.dumps(request.body, indent=4)
                except Exception as e:
                    request.body = ''

        return requests


    def store_request(self, request_data):

        try:
            request_data["body"] = json.loads(request_data["body"])
        except Exception as e:
            request_data["body"] = ''

        headers = []
        for key, value in request_data["headers"].items():
            headers.append({"key": key, "value": request_data["headers"][key]})

        endpoints = self.__endpoint_entity.get_many_by_namespace(request_data["namespace"].id, "created_at", True)

        result = 0
        for endpoint in endpoints:

            if not self.__validate_method(endpoint.method, request_data["method"]):
                continue

            if not self.__validate_uri(endpoint.route, request_data["uri"]):
                continue

            if endpoint.target == "debug":

                self.__request_entity.insert_one({
                    "uri": "/" + request_data["uri"],
                    "method": request_data["method"].lower(),
                    "headers": json.dumps(headers),
                    "body": '{}' if request_data["body"] == '' else json.dumps(request_data["body"]),
                    "status": "debug",
                    "endpoint_id": endpoint.id
                })

                result += 1

            elif endpoint.target == "validate":

                if not self.__validate_body(endpoint.body_rules, equest_data["body"]):
                    continue

                if not self.__validate_headers(endpoint.headers_rules, headers):
                    continue

                self.__request_entity.insert_one({
                    "uri": "/" + request_data["uri"],
                    "method": request_data["method"].lower(),
                    "headers": json.dumps(headers),
                    "body": json.dumps(request_data["body"]),
                    "status": "debug",
                    "endpoint_id": endpoint.id
                })

                result += 1

        return result



    def __validate_uri(self, endpoint_uri, request_uri):
        return re.match("^" + endpoint_uri + "$", "/" + request_uri) != None


    def __validate_method(self, endpoint_method, request_method):
        return endpoint_method.lower() == "any" or endpoint_method.lower() == request_method.lower()


    def __validate_body(self, endpoint_body, request_body):
        return True


    def __validate_headers(self, endpoint_headers, request_headers):
        return True