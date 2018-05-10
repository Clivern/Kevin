"""
Meta Entity Module
"""

# Django
from django.contrib.auth.models import User

# local Django
from app.models import Namespace
from app.models import Endpoint
from app.models import Request
from app.models import User_Meta
from app.models import Namespace_Meta
from app.models import Endpoint_Meta
from app.models import Request_Meta
from app.modules.util.helpers import Helpers


class Meta_Entity():

    NAMESPACE_META="NAMESPACE_META"
    USER_META="USER_META"
    ENDPOINT_META="ENDPOINT_META"
    REQUEST_META="REQUEST_META"


    def insert_one(self, meta, meta_type):
        """Insert a New Meta"""
        if meta_type == self.NAMESPACE_META:
            meta = Namespace_Meta(
                key = meta["key"],
                value = meta["value"],
                user = Namespace.objects.get(pk=meta["user_id"])
            )
        elif meta_type == self.USER_META:
            meta = User_Meta(
                key = meta["key"],
                value = meta["value"],
                user = User.objects.get(pk=meta["user_id"])
            )
        elif meta_type == self.ENDPOINT_META:
            meta = Endpoint_Meta(
                key = meta["key"],
                value = meta["value"],
                user = Endpoint.objects.get(pk=meta["user_id"])
            )
        elif meta_type == self.REQUEST_META:
            meta = Request_Meta(
                key = meta["key"],
                value = meta["value"],
                user = Request.objects.get(pk=meta["user_id"])
            )
        else:
            return False

        meta.save()
        return False if meta.pk is None else meta


    def insert_many(self, metas, meta_type):
        """Insert Many Metas"""
        status = True
        for meta in metas:
            status &= True if self.insert_one(meta, meta_type) != False else False
        return status


    def get_one_by_id(self, id, meta_type):
        """Get Meta By ID"""
        try:
            if meta_type == self.NAMESPACE_META:
                meta = Namespace_Meta.objects.get(pk=id)
            elif meta_type == self.USER_META:
                meta = User_Meta.objects.get(pk=id)
            elif meta_type == self.ENDPOINT_META:
                meta = Endpoint_Meta.objects.get(pk=id)
            elif meta_type == self.REQUEST_META:
                meta = Request_Meta.objects.get(pk=id)
            else:
                return False

            return False if meta.pk is None else meta
        except:
            return False


    def get_one_by_item_id_key(self, item_id, key, meta_type):
        """Get Meta By ID and Key"""
        try:
            if meta_type == self.NAMESPACE_META:
                meta = Namespace_Meta.objects.get(namespace=item_id, key=key)
            elif meta_type == self.USER_META:
                meta = User_Meta.objects.get(user=item_id, key=key)
            elif meta_type == self.ENDPOINT_META:
                meta = Endpoint_Meta.objects.get(endpoint=item_id, key=key)
            elif meta_type == self.REQUEST_META:
                meta = Request_Meta.objects.get(request=item_id, key=key)
            else:
                return False

            return False if meta.pk is None else meta
        except:
            return False


    def get_many_by_key(self, key, meta_type):
        """Get Many Metas By Key"""
        if meta_type == self.NAMESPACE_META:
            metas = Namespace_Meta.objects.filter(key=key)
        elif meta_type == self.USER_META:
            metas = User_Meta.objects.filter(key=key)
        elif meta_type == self.ENDPOINT_META:
            metas = Endpoint_Meta.objects.filter(key=key)
        elif meta_type == self.REQUEST_META:
            metas = Request_Meta.objects.filter(key=key)
        else:
            return False

        return metas


    def get_many_by_item_id(self, item_id, meta_type):
        """Get Many Endpoints By Namespace ID"""
        if meta_type == self.NAMESPACE_META:
            metas = Namespace_Meta.objects.filter(namespace=item_id)
        elif meta_type == self.USER_META:
            metas = User_Meta.objects.filter(user=item_id)
        elif meta_type == self.ENDPOINT_META:
            metas = Endpoint_Meta.objects.filter(endpoint=item_id)
        elif meta_type == self.REQUEST_META:
            metas = Request_Meta.objects.filter(request=item_id)
        else:
            return False

        return metas


    def update_one_by_id(self, id, meta_type, new_data):
        """Update Meta By ID"""
        meta = self.get_one_by_id(id, meta_type)
        if meta != False:
            if "key" in new_data:
                meta.key = new_data["key"]

            if "value" in new_data:
                meta.value = new_data["value"]

            if "namespace_id" in new_data:
                meta.namespace = Namespace.objects.get(pk=new_data["namespace_id"])

            if "user_id" in new_data:
                meta.user = User.objects.get(pk=new_data["user_id"])

            if "endpoint_id" in new_data:
                meta.endpoint = Endpoint.objects.get(pk=new_data["endpoint_id"])

            if "request_id" in new_data:
                meta.request = Request.objects.get(pk=new_data["request_id"])

            meta.save()
            return True
        return False


    def update_one_by_item_id_key(self, item_id, key, meta_type, new_data):
        """Update Meta By Item ID and Key"""
        meta = self.get_one_by_item_id_key(item_id, key, meta_type)
        if meta != False:
            if "key" in new_data:
                meta.key = new_data["key"]

            if "value" in new_data:
                meta.value = new_data["value"]

            if "namespace_id" in new_data:
                meta.namespace = Namespace.objects.get(pk=new_data["namespace_id"])

            if "user_id" in new_data:
                meta.user = User.objects.get(pk=new_data["user_id"])

            if "endpoint_id" in new_data:
                meta.endpoint = Endpoint.objects.get(pk=new_data["endpoint_id"])

            if "request_id" in new_data:
                meta.request = Request.objects.get(pk=new_data["request_id"])

            meta.save()
            return True
        return False


    def delete_one_by_id(self, id, meta_type):
        """Delete Meta By ID"""
        meta = self.get_one_by_id(id, meta_type)
        if meta != False:
            count, deleted = meta.delete()
            return True if count > 0 else False
        return False


    def delete_one_by_item_id_key(self, item_id, key, meta_type):
        """Delete Meta By Item ID and Key"""
        meta = self.get_one_by_item_id_key(item_id, key, meta_type)
        if meta != False:
            count, deleted = meta.delete()
            return True if count > 0 else False
        return False