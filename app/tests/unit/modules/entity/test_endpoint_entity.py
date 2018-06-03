"""
Endpoint Entity Test Cases
"""

from django.test import TestCase
from pprint import pprint
from app.modules.entity.endpoint_entity import Endpoint_Entity
from app.modules.entity.namespace_entity import Namespace_Entity
from django.contrib.auth.models import User


class Test_Endpoint_Entity(TestCase):


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
        namespace = namespace_entity.insert_one({
            "name": "kevin",
            "is_public": True,
            "user_id": user.pk
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
        namespace = namespace_entity.insert_one({
            "name": "kevin",
            "is_public": True,
            "user_id": user.pk
        })
        self.assertTrue(namespace)
        self.assertTrue(namespace.id > 0)
        endpoint_entity = Endpoint_Entity();
        self.assertTrue(endpoint_entity.insert_many([
            {"route": "/", "method": Endpoint_Entity.GET, "target": Endpoint_Entity.DEBUG, "route_rules": "{}", "headers_rules": "{}", "body_rules": "{}","namespace_id": namespace.id},
            {"route": "/", "method": Endpoint_Entity.POST, "target": Endpoint_Entity.VALIDATE, "route_rules": "{}", "headers_rules": "{}", "body_rules": "{}","namespace_id": namespace.id},
            {"route": "/{id}", "method": Endpoint_Entity.GET, "target": Endpoint_Entity.DYNAMIC, "route_rules": "{}", "headers_rules": "{}", "body_rules": "{}","namespace_id": namespace.id},
        ]))


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
        namespace = namespace_entity.insert_one({
            "name": "kevin",
            "is_public": True,
            "user_id": user.pk
        })
        self.assertTrue(namespace)
        self.assertTrue(namespace.id > 0)
        endpoint_entity = Endpoint_Entity();
        entity = endpoint_entity.insert_one({
            "route": "/",
            "method": Endpoint_Entity.GET,
            "target": Endpoint_Entity.DEBUG,
            "route_rules": "{}",
            "headers_rules": "{}",
            "body_rules": "{}",
            "namespace_id": namespace.id
        })
        entity = endpoint_entity.get_one_by_id(entity.id)
        self.assertEqual("get/debug", entity.method + entity.route + entity.target)


    def test_get_many_by_namespace(self):
        user = User(
            first_name = "Joe",
            last_name = "Doe",
            username = "joe",
            email = "joe@kevin.com",
            password = "joe_doe"
        )
        user.save()
        namespace_entity = Namespace_Entity()
        namespace = namespace_entity.insert_one({
            "name": "kevin",
            "is_public": True,
            "user_id": user.pk
        })
        self.assertTrue(namespace)
        self.assertTrue(namespace.id > 0)
        endpoint_entity = Endpoint_Entity();
        self.assertTrue(endpoint_entity.insert_many([
            {"route": "/", "method": Endpoint_Entity.GET, "target": Endpoint_Entity.DEBUG, "route_rules": "{}", "headers_rules": "{}", "body_rules": "{}","namespace_id": namespace.id},
            {"route": "/", "method": Endpoint_Entity.POST, "target": Endpoint_Entity.VALIDATE, "route_rules": "{}", "headers_rules": "{}", "body_rules": "{}","namespace_id": namespace.id},
            {"route": "/{id}", "method": Endpoint_Entity.GET, "target": Endpoint_Entity.DYNAMIC, "route_rules": "{}", "headers_rules": "{}", "body_rules": "{}","namespace_id": namespace.id},
        ]))
        self.assertEqual(3, endpoint_entity.get_many_by_namespace(namespace.id, "created_at", False).count())


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
        namespace = namespace_entity.insert_one({
            "name": "kevin",
            "is_public": True,
            "user_id": user.pk
        })
        self.assertTrue(namespace)
        self.assertTrue(namespace.id > 0)
        endpoint_entity = Endpoint_Entity();
        entity = endpoint_entity.insert_one({
            "route": "/",
            "method": Endpoint_Entity.GET,
            "target": Endpoint_Entity.DEBUG,
            "route_rules": "{}",
            "headers_rules": "{}",
            "body_rules": "{}",
            "namespace_id": namespace.id
        })
        self.assertTrue(endpoint_entity.update_one_by_id(entity.id, {"route": "/ips"}))
        entity = endpoint_entity.get_one_by_id(entity.id)
        self.assertEqual("get/ipsdebug", entity.method + entity.route + entity.target)


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
        namespace = namespace_entity.insert_one({
            "name": "kevin",
            "is_public": True,
            "user_id": user.pk
        })
        self.assertTrue(namespace)
        self.assertTrue(namespace.id > 0)
        endpoint_entity = Endpoint_Entity();
        entity = endpoint_entity.insert_one({
            "route": "/",
            "method": Endpoint_Entity.GET,
            "target": Endpoint_Entity.DEBUG,
            "route_rules": "{}",
            "headers_rules": "{}",
            "body_rules": "{}",
            "namespace_id": namespace.id
        })
        self.assertTrue(entity)
        self.assertTrue(endpoint_entity.delete_one_by_id(entity.id))
        self.assertFalse(endpoint_entity.delete_one_by_id(1000))
