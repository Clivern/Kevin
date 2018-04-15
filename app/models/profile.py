"""
Profile Model
"""

from django.conf import settings
from django.db import models

class Profile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_index=True
    )
    access_token = models.CharField(max_length=200)
    refresh_token = models.CharField(max_length=200)
    access_token_updated_at = models.DateTimeField()
    refresh_token_updated_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)