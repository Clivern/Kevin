"""
Option Model
"""

from django.db import models

class Option(models.Model):

    AUTOLOAD_CHOICES = (
        ('on', 'On'),
        ('off', 'Off')
    )

    key = models.CharField(max_length=30, db_index=True)
    value = models.CharField(max_length=200)
    autoload = models.CharField(max_length=5, choices=AUTOLOAD_CHOICES, default="off")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)