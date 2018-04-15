"""
Request Meta Model
"""

from django.db import models
from .request import Request

class Request_Meta(models.Model):
    request = models.ForeignKey(
        Request,
        on_delete=models.CASCADE,
        verbose_name="Request",
        db_index=True
    )
    key = models.CharField(max_length=30, verbose_name="Key", db_index=True)
    value = models.CharField(max_length=200, verbose_name= "Value")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created_at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated_at")