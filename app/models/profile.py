"""
Profile Model
"""

from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        db_index=True,
        verbose_name="Related user"
    )
    access_token = models.CharField(max_length=200, verbose_name="Access token")
    refresh_token = models.CharField(max_length=200, verbose_name="Refresh token")
    access_token_updated_at = models.DateTimeField(verbose_name="Access token last update")
    refresh_token_updated_at = models.DateTimeField(verbose_name="Refresh token last update")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")