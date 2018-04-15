"""
Endpoint Meta Model
"""

from django.db import models
from .endpoint import Endpoint

class Endpoint_Meta(models.Model):

    endpoint = models.ForeignKey(
        Endpoint,
        on_delete=models.CASCADE,
        db_index=True
    )
    key = models.CharField(max_length=30, db_index=True)
    value = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)