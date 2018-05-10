"""
Endpoint Model
"""

# Django
from django.db import models

# local Django
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
        ('debug', 'DEBUG'),
        ('dynamic', 'DYNAMIC'),
    )

    namespace = models.ForeignKey(
        Namespace,
        on_delete=models.CASCADE,
        db_index=True,
        verbose_name="Related namespace"
    )

    route = models.CharField(max_length=100, verbose_name="Route")
    method = models.CharField(max_length=20, choices=METHOD_CHOICES, default="any", verbose_name="Method")
    target = models.CharField(max_length=20, choices=TARGET_CHOICES, default="debug", verbose_name="Target")
    route_rules = models.TextField(verbose_name="Route rules")
    headers_rules = models.TextField(verbose_name="Headers rules")
    body_rules = models.TextField(verbose_name="Body rules")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")


    def __str__(self):
        return "%s /%s" % (self.method, self.route)