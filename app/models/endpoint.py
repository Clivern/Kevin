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
        verbose_name="Namespace",
        db_index=True
    )
    route = models.CharField(max_length=100, verbose_name="Route")
    method = models.CharField(max_length=20, choices=METHOD_CHOICES, default="any", verbose_name="Method")
    target = models.CharField(max_length=20, choices=TARGET_CHOICES, default="debug", verbose_name="Target")
    route_rules = models.TextField(verbose_name="Route_Rules")
    header_rules = models.TextField(verbose_name="Header_Rules")
    body_rules = models.TextField(verbose_name="Body_Rules")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created_at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated_at")