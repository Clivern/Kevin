"""
Option Model
"""

from django.db import models

class Option(models.Model):

    AUTOLOAD_CHOICES = (
        ('on', 'On'),
        ('off', 'Off')
    )

    key = models.CharField(max_length=30, db_index=True, verbose_name="Key")
    value = models.CharField(max_length=200, verbose_name="Value")
    autoload = models.CharField(max_length=5, choices=AUTOLOAD_CHOICES, default="off", verbose_name="Autoload")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")