"""
Request Meta Model
"""

# Django
from django.db import models

# local Django
from .request import Request


class Request_Meta(models.Model):

    request = models.ForeignKey(
        Request,
        on_delete=models.CASCADE,
        db_index=True,
        verbose_name="Related request"
    )
    key = models.CharField(max_length=30, db_index=True, verbose_name="Meta key")
    value = models.CharField(max_length=200, verbose_name="Meta value")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")


    def __str__(self):
        return self.key