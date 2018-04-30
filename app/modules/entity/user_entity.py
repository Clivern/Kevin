"""
User Entity Module
"""

from django.contrib.auth.models import User
from app.modules.util.helpers import Helpers
from app.models import Profile
from app.models import User_Meta
from django.contrib.auth.hashers import make_password

class User_Entity():

    def insert_one(self, user):
        """Insert a New User"""
        if self.get_one_by_username(user["username"]) != False:
            return False

        new_user = User()
        if "username" in user:
            new_user.username = user["username"]

        if "first_name" in user:
            new_user.first_name = user["first_name"]

        if "last_name" in user:
            new_user.last_name = user["last_name"]

        if "email" in user:
            new_user.email = user["email"]

        if "password" in user:
            new_user.password = make_password(user["password"])

        if "is_staff" in user:
            new_user.is_staff = user["is_staff"]

        if "is_active" in user:
            new_user.is_active = user["is_active"]

        if "is_superuser" in user:
            new_user.is_superuser = user["is_superuser"]

        if "last_login" in user:
            new_user.last_login = user["last_login"]

        if "date_joined" in user:
            new_user.date_joined = user["date_joined"]

        new_user.save()
        return False if new_user.pk is None else new_user

    def get_one_by_username(self, username):
        """Get User By Username"""
        try:
            user = User.objects.get(username=username)
            return False if user.pk is None else user
        except:
            return False


    def get_one_by_email(self, email):
        """Get User By Email"""
        try:
            user = User.objects.get(email=email)
            return False if user.pk is None else user
        except:
            return False