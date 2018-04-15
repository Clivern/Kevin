"""
Endpoint Model
"""

from django.db import models
from .namespace import Namespace

class Endpoint(models.Model):

    METHOD_CHOICES = (
        ('get', 'GET'),
        ('post', 'POST'),
        ('head', 'HEAD'),
        ('put', 'PUT'),
        ('delete', 'DELETE'),
        ('patch', 'PATCH'),
        ('trace', 'TRACE'),
        ('options', 'OPTIONS'),
        ('connect', 'CONNECT'),
        ('any', 'ANY')
    )
    TARGET_CHOICES = (
        ('validate', 'VALIDATE'),
        ('debug', 'DEBUG')
    )

    namespace = models.ForeignKey(
        Namespace,
        on_delete=models.CASCADE,
        db_index=True
    )
    route = models.CharField(max_length=100)
    method = models.CharField(max_length=20, choices=METHOD_CHOICES, default="any")
    target = models.CharField(max_length=20, choices=TARGET_CHOICES, default="debug")
    route_rules = models.TextField()
    headers_rules = models.TextField()
    body_rules = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)