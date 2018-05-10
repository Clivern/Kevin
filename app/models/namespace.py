"""
Namespace Model
"""

# Django
from django.db import models
from django.contrib.auth.models import User


class Namespace(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_index=True,
        verbose_name="Related user"
    )
    name = models.CharField(max_length=50, verbose_name="Name")
    slug = models.SlugField(max_length=60, unique=True, db_index=True, verbose_name="Slug")
    is_public = models.BooleanField(default=False, verbose_name="Is Public")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")