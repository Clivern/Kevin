"""
Request Entity Test Cases
"""

from django.test import TestCase
from pprint import pprint
from app.modules.entity.namespace_entity import Namespace_Entity
from app.modules.entity.endpoint_entity import Endpoint_Entity
from app.modules.entity.request_entity import Request_Entity
from django.contrib.auth.models import User


class Test_Request_Entity(TestCase):

    def test_insert_one(self):
        user = User(
            first_name = "Joe",
            last_name = "Doe",
            username = "joe",
            email = "joe@kevin.com",
            password = "joe_doe"
        )
        user.save()
        namespace_entity = Namespace_Entity()
        endpoint_entity = Endpoint_Entity()
        request_entity = Request_Entity()
        namespace = namespace_entity.insert_one({
            "name": "kevin",
            "is_public": True,
            "user_id": user.pk
        })
        endpoint = endpoint_entity.insert_one({
            "route": "/",
            "method": Endpoint_Entity.GET,
            "target": Endpoint_Entity.DEBUG,
            "route_rules": "{}",
            "headers_rules": "{}",
            "body_rules": "{}",
            "namespace_id": namespace.id
        })
        self.assertTrue(namespace)
        self.assertTrue(namespace.id > 0)
        endpoint_entity = Endpoint_Entity();
        self.assertTrue(endpoint_entity.insert_one({
            "route": "/",
            "method": Endpoint_Entity.GET,
            "target": Endpoint_Entity.DEBUG,
            "route_rules": "{}",
            "headers_rules": "{}",
            "body_rules": "{}",
            "namespace_id": namespace.id
        }))
        request = request_entity.insert_one({
            "uri": "/",
            "method": Request_Entity.GET,
            "headers": "{}",
            "body": "{}",
            "status": Request_Entity.DEBUG,
            "endpoint_id": endpoint.id
        })
        self.assertTrue(request)
        self.assertTrue(request.id > 0)


    def test_insert_many(self):
        user = User(
            first_name = "Joe",
            last_name = "Doe",
            username = "joe",
            email = "joe@kevin.com",
            password = "joe_doe"
        )
        user.save()
        namespace_entity = Namespace_Entity()
        endpoint_entity = Endpoint_Entity()
        request_entity = Request_Entity()
        namespace = namespace_entity.insert_one({
            "name": "kevin",
            "is_public": True,
            "user_id": user.pk
        })
        endpoint = endpoint_entity.insert_one({
            "route": "/",
            "method": Endpoint_Entity.GET,
            "target": Endpoint_Entity.DEBUG,
            "route_rules": "{}",
            "headers_rules": "{}",
            "body_rules": "{}",
            "namespace_id": namespace.id
        })
        self.assertTrue(namespace)
        self.assertTrue(namespace.id > 0)
        endpoint_entity = Endpoint_Entity();
        self.assertTrue(endpoint_entity.insert_one({
            "route": "/",
            "method": Endpoint_Entity.GET,
            "target": Endpoint_Entity.DEBUG,
            "route_rules": "{}",
            "headers_rules": "{}",
            "body_rules": "{}",
            "namespace_id": namespace.id
        }))
        request = request_entity.insert_many([
            {"uri": "/","method": Request_Entity.GET,"headers": "{}","body": "{}","status": Request_Entity.DEBUG,"endpoint_id": endpoint.id},
            {"uri": "/","method": Request_Entity.POST,"headers": "{}","body": "{}","status": Request_Entity.DEBUG,"endpoint_id": endpoint.id},
            {"uri": "/{id}","method": Request_Entity.GET,"headers": "{}","body": "{}","status": Request_Entity.DEBUG,"endpoint_id": endpoint.id},
            {"uri": "/{id}","method": Request_Entity.PUT,"headers": "{}","body": "{}","status": Request_Entity.DEBUG,"endpoint_id": endpoint.id}
        ])
        self.assertTrue(request)


    def test_get_one_by_id(self):
        user = User(
            first_name = "Joe",
            last_name = "Doe",
            username = "joe",
            email = "joe@kevin.com",
            password = "joe_doe"
        )
        user.save()
        namespace_entity = Namespace_Entity()
        endpoint_entity = Endpoint_Entity()
        request_entity = Request_Entity()
        namespace = namespace_entity.insert_one({
            "name": "kevin",
            "is_public": True,
            "user_id": user.pk
        })
        endpoint = endpoint_entity.insert_one({
            "route": "/",
            "method": Endpoint_Entity.GET,
            "target": Endpoint_Entity.DEBUG,
            "route_rules": "{}",
            "headers_rules": "{}",
            "body_rules": "{}",
            "namespace_id": namespace.id
        })
        self.assertTrue(namespace)
        self.assertTrue(namespace.id > 0)
        endpoint_entity = Endpoint_Entity();
        self.assertTrue(endpoint_entity.insert_one({
            "route": "/",
            "method": Endpoint_Entity.GET,
            "target": Endpoint_Entity.DEBUG,
            "route_rules": "{}",
            "headers_rules": "{}",
            "body_rules": "{}",
            "namespace_id": namespace.id
        }))
        request = request_entity.insert_one({
            "uri": "/",
            "method": Request_Entity.GET,
            "headers": "{}",
            "body": "{}",
            "status": Request_Entity.DEBUG,
            "endpoint_id": endpoint.id
        })
        self.assertTrue(request)
        self.assertTrue(request.id > 0)
        request = request_entity.get_one_by_id(request.id)
        self.assertEqual("get/debug", request.method + request.uri + request.status)


    def test_get_many_by_endpoint(self):
        user = User(
            first_name = "Joe",
            last_name = "Doe",
            username = "joe",
            email = "joe@kevin.com",
            password = "joe_doe"
        )
        user.save()
        namespace_entity = Namespace_Entity()
        endpoint_entity = Endpoint_Entity()
        request_entity = Request_Entity()
        namespace = namespace_entity.insert_one({
            "name": "kevin",
            "is_public": True,
            "user_id": user.pk
        })
        endpoint = endpoint_entity.insert_one({
            "route": "/",
            "method": Endpoint_Entity.GET,
            "target": Endpoint_Entity.DEBUG,
            "route_rules": "{}",
            "headers_rules": "{}",
            "body_rules": "{}",
            "namespace_id": namespace.id
        })
        self.assertTrue(namespace)
        self.assertTrue(namespace.id > 0)
        endpoint_entity = Endpoint_Entity();
        self.assertTrue(endpoint_entity.insert_one({
            "route": "/",
            "method": Endpoint_Entity.GET,
            "target": Endpoint_Entity.DEBUG,
            "route_rules": "{}",
            "headers_rules": "{}",
            "body_rules": "{}",
            "namespace_id": namespace.id
        }))
        request = request_entity.insert_many([
            {"uri": "/","method": Request_Entity.GET,"headers": "{}","body": "{}","status": Request_Entity.DEBUG,"endpoint_id": endpoint.id},
            {"uri": "/","method": Request_Entity.POST,"headers": "{}","body": "{}","status": Request_Entity.DEBUG,"endpoint_id": endpoint.id},
            {"uri": "/{id}","method": Request_Entity.GET,"headers": "{}","body": "{}","status": Request_Entity.DEBUG,"endpoint_id": endpoint.id},
            {"uri": "/{id}","method": Request_Entity.PUT,"headers": "{}","body": "{}","status": Request_Entity.DEBUG,"endpoint_id": endpoint.id}
        ])
        self.assertEqual(request_entity.get_many_by_endpoint(endpoint.id, "create_at", True).count(), 4)

    def test_update_one_by_id(self):
        user = User(
            first_name = "Joe",
            last_name = "Doe",
            username = "joe",
            email = "joe@kevin.com",
            password = "joe_doe"
        )
        user.save()
        namespace_entity = Namespace_Entity()
        endpoint_entity = Endpoint_Entity()
        request_entity = Request_Entity()
        namespace = namespace_entity.insert_one({
            "name": "kevin",
            "is_public": True,
            "user_id": user.pk
        })
        endpoint = endpoint_entity.insert_one({
            "route": "/",
            "method": Endpoint_Entity.GET,
            "target": Endpoint_Entity.DEBUG,
            "route_rules": "{}",
            "headers_rules": "{}",
            "body_rules": "{}",
            "namespace_id": namespace.id
        })
        self.assertTrue(namespace)
        self.assertTrue(namespace.id > 0)
        endpoint_entity = Endpoint_Entity();
        self.assertTrue(endpoint_entity.insert_one({
            "route": "/",
            "method": Endpoint_Entity.GET,
            "target": Endpoint_Entity.DEBUG,
            "route_rules": "{}",
            "headers_rules": "{}",
            "body_rules": "{}",
            "namespace_id": namespace.id
        }))
        request = request_entity.insert_one({
            "uri": "/",
            "method": Request_Entity.GET,
            "headers": "{}",
            "body": "{}",
            "status": Request_Entity.DEBUG,
            "endpoint_id": endpoint.id
        })
        self.assertTrue(request)
        self.assertTrue(request.id > 0)
        self.assertTrue(request_entity.update_one_by_id(request.id, {"uri" : "/new"}))
        request = request_entity.get_one_by_id(request.id)
        self.assertEqual("get/newdebug", request.method + request.uri + request.status)


    def test_delete_one_by_id(self):
        user = User(
            first_name = "Joe",
            last_name = "Doe",
            username = "joe",
            email = "joe@kevin.com",
            password = "joe_doe"
        )
        user.save()
        namespace_entity = Namespace_Entity()
        endpoint_entity = Endpoint_Entity()
        request_entity = Request_Entity()
        namespace = namespace_entity.insert_one({
            "name": "kevin",
            "is_public": True,
            "user_id": user.pk
        })
        endpoint = endpoint_entity.insert_one({
            "route": "/",
            "method": Endpoint_Entity.GET,
            "target": Endpoint_Entity.DEBUG,
            "route_rules": "{}",
            "headers_rules": "{}",
            "body_rules": "{}",
            "namespace_id": namespace.id
        })
        self.assertTrue(namespace)
        self.assertTrue(namespace.id > 0)
        endpoint_entity = Endpoint_Entity();
        self.assertTrue(endpoint_entity.insert_one({
            "route": "/",
            "method": Endpoint_Entity.GET,
            "target": Endpoint_Entity.DEBUG,
            "route_rules": "{}",
            "headers_rules": "{}",
            "body_rules": "{}",
            "namespace_id": namespace.id
        }))
        request = request_entity.insert_one({
            "uri": "/",
            "method": Request_Entity.GET,
            "headers": "{}",
            "body": "{}",
            "status": Request_Entity.DEBUG,
            "endpoint_id": endpoint.id
        })
        self.assertTrue(request)
        self.assertTrue(request.id > 0)
        self.assertTrue(request_entity.delete_one_by_id(request.id))
        self.assertFalse(request_entity.delete_one_by_id(1000))