"""
Kevin Info Command

see https://docs.djangoproject.com/en/2.0/howto/custom-management-commands/
"""

import os
import time
import json
from app.settings.info import *
from django.core.management import utils
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from app.modules.entity.job_entity import Job_Entity
from importlib import import_module

class Command(BaseCommand):

    help = "Run Kevin Schedule!"

    available = [
        "run"
    ]

    _job_entity = Job_Entity()

    def add_arguments(self, parser):
        """Config Command Args"""
        parser.add_argument('command', type=str, nargs='+', help='Available commands are %s' % ", ".join(self.available))


    def handle(self, *args, **options):
        """Command Handle"""
        if len(options['command']) == 0 or options['command'][0] not in self.available:
            raise CommandError('Command Does not exist! Please use one of the following: python manage.py schedule [%s]' % ", ".join(self.available))

        if options['command'][0] == "run":
            self.stdout.write(self.style.SUCCESS("█ Running Kevin Schedule...\n"))
            while True:
                job = self._get_job()
                if job != False:
                    self.run(job)
                time.sleep(2)

    def _get_job(self):
        return {"executor":"test.Test", "parameters":"{\"text\": \"Job Text\"}"}

    def run(self, job):
        try:
            job_module = job["executor"].split(".")
            p = import_module("app.jobs.%s" % (job_module[0]))
            c = getattr(p, job_module[1])
            instance = c(json.loads(job["parameters"]))
            if instance.execute():
                return True
            else:
                return False
        except Exception as e:
            return False