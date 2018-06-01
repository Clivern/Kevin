"""
Namespace Entity Module
"""

# Django
from django.contrib.auth.models import User

# local Django
from app.models import Namespace
from app.models import Namespace_Meta
from app.modules.util.helpers import Helpers


class Namespace_Entity():


    def insert_one(self, namespace):
        """Insert a New Namespace"""
        if "slug" not in namespace:
            namespace["slug"] = Helpers().slugify(namespace["name"])

        namespace = Namespace(
            name=namespace["name"],
            slug=namespace["slug"],
            is_public=namespace["is_public"] if "is_public" in namespace else False,
            user=User.objects.get(pk=namespace["user_id"])
        )

        namespace.save()
        return False if namespace.pk is None else namespace


    def insert_many(self, namespaces):
        """Insert Many Namespaces"""
        status = True
        for namespace in namespaces:
            status &= True if self.insert_one(namespace) != False else False
        return status


    def get_one_by_id(self, id):
        """Get Namespace By ID"""
        try:
            namespace = Namespace.objects.get(pk=id)
            return False if namespace.pk is None else namespace
        except:
            return False


    def user_owns(self, namespace_id, user_id):
        """Get Namespace By ID and User ID"""
        try:
            namespace = Namespace.objects.get(pk=namespace_id, user=user_id)
            return False if namespace.pk is None else True
        except:
            return False


    def get_one_by_slug(self, slug):
        """Get Namespace By Slug"""
        try:
            namespace = Namespace.objects.get(slug=slug)
            return False if namespace.pk is None else namespace
        except:
            return False


    def get_many_by_user(self, user_id, order_by, asc):
        """Get Many Namespaces By User ID"""
        namespaces = Namespace.objects.filter(user=user_id).order_by(order_by if asc else "-created_at")
        return namespaces


    def update_one_by_id(self, id, new_data):
        """Update Namespace By ID"""
        namespace = self.get_one_by_id(id)
        if namespace != False:
            if "name" in new_data:
                namespace.name = new_data["name"]

            if "slug" in new_data and not self.get_one_by_slug(new_data["slug"]):
                namespace.slug = new_data["slug"]

            if "is_public" in new_data:
                namespace.is_public = new_data["is_public"] if "is_public" in new_data else False

            if "user_id" in new_data:
                namespace.user = User.objects.get(pk=new_data["user_id"])

            namespace.save()
            return True
        return False


    def update_one_by_slug(self, slug, new_data):
        """Update Namespace By Slug"""
        namespace = self.get_one_by_slug(slug)
        if namespace != False:
            if "name" in new_data:
                namespace.name = new_data["name"]

            if "slug" in new_data and not self.get_one_by_slug(new_data["slug"]):
                namespace.slug = new_data["slug"]

            if "is_public" in new_data:
                namespace.is_public = new_data["is_public"] if "is_public" in new_data else False

            if "user_id" in new_data:
                namespace.user = User.objects.get(pk=new_data["user_id"])

            namespace.save()
            return True
        return False


    def delete_one_by_id(self, id):
        """Delete Namespace By ID"""
        namespace = self.get_one_by_id(id)
        if namespace != False:
            count, deleted = namespace.delete()
            return True if count > 0 else False
        return False


    def delete_one_by_slug(self, slug):
        """Delete Namespace By Slug"""
        namespace = self.get_one_by_slug(slug)
        if namespace != False:
            count, deleted = namespace.delete()
            return True if count > 0 else False
        return False