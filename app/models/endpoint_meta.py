"""
Endpoint Meta Model
"""

from django.db import models
from .endpoint import Endpoint

class Endpoint_Meta(models.Model):

    endpoint = models.ForeignKey(
        Endpoint,
        on_delete=models.CASCADE,
        db_index=True,
        verbose_name="Related endpoint"
    )
    key = models.CharField(max_length=30, db_index=True, verbose_name="Meta key")
    value = models.CharField(max_length=200, verbose_name="Meta value")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    def __str__(self):
        return self.key