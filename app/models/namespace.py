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
        verbose_name="User",
        db_index=True
    )
    name = models.CharField(max_length=50, verbose_name="Name")
    slug = models.CharField(max_length=60, unique=True, db_index=True, verbose_name="Slug")
    is_public = models.CharField(max_length=5, choices=IS_PUBLIC_CHOICES, default="no", verbose_name="Is_Public")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created_at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated_at")