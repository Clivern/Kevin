"""
Request Model
"""

from django.db import models
from .endpoint import Endpoint

class Request(models.Model):

    METHOD_CHOICES = (
        ('get', 'GET'),
        ('post', 'POST'),
        ('head', 'HEAD'),
        ('put', 'PUT'),
        ('delete', 'DELETE'),
        ('patch', 'PATCH'),
        ('trace', 'TRACE'),
        ('options', 'OPTIONS'),
        ('connect', 'CONNECT')
    )

    STATUS_CHOICES = (
        ('valid', 'VALID'),
        ('not_valid', 'NOT_VALID'),
        ('debug', 'DEBUG'),
    )

    endpoint = models.ForeignKey(
        Endpoint,
        on_delete=models.CASCADE,
        db_index=True
    )

    method = models.CharField(max_length=20, choices=METHOD_CHOICES, default="get")
    uri = models.TextField()
    headers = models.TextField()
    body = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="debug")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)