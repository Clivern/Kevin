"""
Namespace Entity Test Cases
"""

from django.test import TestCase
from pprint import pprint
from app.modules.entity.namespace_entity import Namespace_Entity
from django.contrib.auth.models import User


class Test_Namespace_Entity(TestCase):

    def test_insert_one(self):
        user1 = User(
            first_name = "Joe1",
            last_name = "Doe1",
            username = "joe1",
            email = "joe1@kevin.com",
            password = "joe1_doe"
        )
        user1.save()
        namespace_entity = Namespace_Entity()
        namespace = namespace_entity.insert_one({
            "name": "kevin1",
            "is_public": True,
            "user_id": user1.pk
        })
        self.assertTrue(namespace)
        self.assertTrue(namespace.id > 0)


    def test_insert_many(self):
        user2 = User(
            first_name = "Joe2",
            last_name = "Doe2",
            username = "joe2",
            email = "joe2@kevin.com",
            password = "joe2_doe"
        )
        user3 = User(
            first_name = "Joe3",
            last_name = "Doe3",
            username = "joe3",
            email = "joe3@kevin.com",
            password = "joe3_doe"
        )
        user2.save()
        user3.save()

        namespace_entity = Namespace_Entity()
        self.assertTrue(namespace_entity.insert_many([
            {"name": "kevin2","is_public": True,"user_id": user2.pk},
            {"name": "kevin3","is_public": False,"user_id": user3.pk},
            {"name": "kevin4","is_public": True,"user_id": user2.pk},
            {"name": "kevin5","is_public": False,"user_id": user3.pk}
        ]))


    def test_get_one_by_id(self):
        user4 = User(
            first_name = "Joe4",
            last_name = "Doe4",
            username = "joe4",
            email = "joe4@kevin.com",
            password = "joe4_doe"
        )
        user4.save()
        namespace_entity = Namespace_Entity()
        namespace = namespace_entity.insert_one({
            "name": "kevin Item 6",
            "is_public": False,
            "user_id": user4.pk
        })
        self.assertTrue(namespace)
        self.assertTrue(namespace.id > 0)
        self.assertEqual(namespace.slug, "kevin-item-6")
        self.assertEqual(namespace.name, "kevin Item 6")
        namespace = namespace_entity.get_one_by_id(namespace.id)
        self.assertTrue(namespace.id > 0)
        self.assertEqual(namespace.slug, "kevin-item-6")
        self.assertEqual(namespace.name, "kevin Item 6")


    def test_get_one_by_slug(self):
        user5 = User(
            first_name = "Joe5",
            last_name = "Doe5",
            username = "joe5",
            email = "joe5@kevin.com",
            password = "joe5_doe"
        )
        user5.save()
        namespace_entity = Namespace_Entity()
        namespace = namespace_entity.insert_one({
            "name": "kEvIn ItEM  7",
            "is_public": True,
            "user_id": user5.pk
        })
        self.assertTrue(namespace)
        self.assertTrue(namespace.id > 0)
        self.assertEqual(namespace.slug, "kevin-item-7")
        self.assertEqual(namespace.name, "kEvIn ItEM  7")
        namespace = namespace_entity.get_one_by_slug("kevin-item-7")
        self.assertTrue(namespace.id > 0)
        self.assertEqual(namespace.slug, "kevin-item-7")
        self.assertEqual(namespace.name, "kEvIn ItEM  7")


    def test_delete_one_by_id(self):
        user9 = User(
            first_name = "Joe9",
            last_name = "Doe9",
            username = "joe9",
            email = "joe9@kevin.com",
            password = "joe9_doe"
        )
        user9.save()
        namespace_entity = Namespace_Entity()
        namespace = namespace_entity.insert_one({
            "name": "KeVIN ITEm 9",
            "is_public": True,
            "user_id": user9.pk
        })
        self.assertTrue(namespace)
        self.assertTrue(namespace_entity.delete_one_by_id(namespace.pk))


    def test_delete_one_by_slug(self):
        user10 = User(
            first_name = "Joe10",
            last_name = "Doe10",
            username = "joe10",
            email = "joe10@kevin.com",
            password = "joe10_doe"
        )
        user10.save()
        namespace_entity = Namespace_Entity()
        namespace = namespace_entity.insert_one({
            "name": "KeVIN ITEm 10",
            "is_public": True,
            "user_id": user10.pk
        })
        self.assertTrue(namespace)
        self.assertTrue(namespace_entity.delete_one_by_slug("kevin-item-10"))


    def test_update_one_by_id(self):
        user11 = User(
            first_name = "Joe11",
            last_name = "Doe11",
            username = "joe11",
            email = "joe11@kevin.com",
            password = "joe11_doe"
        )
        user11.save()
        namespace_entity = Namespace_Entity()
        namespace = namespace_entity.insert_one({
            "name": "KeVIN ITEm 20",
            "is_public": True,
            "user_id": user11.pk
        })
        self.assertTrue(namespace)
        self.assertTrue(namespace_entity.update_one_by_id(namespace.id, {
            "name": "KeVIN ITEm 30",
            "is_public": False
        }))


    def test_update_one_by_slug(self):
        user12 = User(
            first_name = "Joe12",
            last_name = "Doe12",
            username = "joe12",
            email = "joe12@kevin.com",
            password = "joe12_doe"
        )
        user12.save()
        namespace_entity = Namespace_Entity()
        namespace = namespace_entity.insert_one({
            "name": "KeVIN ITEm 30",
            "is_public": False,
            "user_id": user12.pk
        })
        self.assertTrue(namespace)
        self.assertTrue(namespace_entity.update_one_by_slug("kevin-item-30", {
            "name": "KeVIN ITEm 30",
            "is_public": True
        }))


    def test_get_many_by_user(self):
        user13 = User(
            first_name = "Joe13",
            last_name = "Doe13",
            username = "joe13",
            email = "joe13@kevin.com",
            password = "joe13_doe"
        )
        user13.save()
        namespace_entity = Namespace_Entity()
        self.assertTrue(namespace_entity.insert_many([
            {"name": "kev Item 1","is_public": True,"user_id": user13.pk},
            {"name": "kev Item 2","is_public": False,"user_id": user13.pk},
            {"name": "kev Item 3","is_public": True,"user_id": user13.pk},
            {"name": "kev Item 4","is_public": False,"user_id": user13.pk}
        ]))
        self.assertEqual(namespace_entity.get_many_by_user(user13.pk, "created_at", True).count(), 4)