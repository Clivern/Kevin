"""
Profile Model
"""

from django.conf import settings
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="User",
        db_index=True
    )
    access_token = models.CharField(max_length=200, verbose_name="Access_Token")
    refresh_token = models.CharField(max_length=200, verbose_name="Refresh_Token")
    access_token_updated_at = models.DateTimeField(verbose_name="Access_Token_Updated_at")
    refresh_token_updated_at = models.DateTimeField(verbose_name="Refresh_Token_Updated_at")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created_at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated_at")