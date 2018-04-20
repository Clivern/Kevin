"""
User Entity Module
"""

from django.contrib.auth.models import User
from app.modules.util.helpers import Helpers
from app.models import Profile
from app.models import User_Meta

class User_Entity():


    def add_meta(self, meta):
        meta = User_Meta(
            key = meta["key"],
            value = meta["value"],
            user = User.objects.get(pk=meta["user_id"])
        )
        meta.save()
        return False if meta.pk is None else meta


    def add_metas(self, metas):
        status = True
        for meta in metas:
            status &= True if self.add_meta(meta) != False else False
        return status


    def delete_meta_by_id(self, id):
        endpoint = self.get_one_by_id(id)
        if endpoint != False:
            count, deleted = endpoint.delete()
            return True if count > 0 else False
        return False

    def delete_metas_by_user(self, where):
        pass

    def update_meta(self, meta, where):
        pass

    def get_meta(self, where):
        pass

    def get_metas(self, where):
        pass