"""
Namespace Model
"""

from django.conf import settings
from django.db import models

class Namespace(models.Model):

    IS_PUBLIC_CHOICES = (
        ('yes', 'Yes'),
        ('no', 'No')
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_index=True
    )
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=60, unique=True, db_index=True)
    is_public = models.CharField(max_length=5, choices=IS_PUBLIC_CHOICES, default="no")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)