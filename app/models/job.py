"""
Job Model
"""

from django.db import models

class Job(models.Model):

    STATUS_CHOICES = (
        ('pending', 'PENDING'),
        ('failed', 'FAILED'),
        ('passed', 'PASSED'),
        ('daemon', 'DAEMON'),
    )

    name = models.CharField(max_length=30, verbose_name="Name")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending", verbose_name="Status")
    executor = models.CharField(max_length=200, verbose_name="Executor")
    parameters = models.TextField(max_length=30, verbose_name="Parameters")
    interval = models.CharField(max_length=30, verbose_name="Interval")
    retry_count = models.PositiveSmallIntegerField(verbose_name="Retry Count")
    priority = models.PositiveSmallIntegerField(verbose_name="Priority")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    run_at = models.DateTimeField(verbose_name="Run at")
    last_run = models.DateTimeField(verbose_name="Last Run")