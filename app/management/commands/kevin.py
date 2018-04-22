"""
Kevin Info Command
"""

from django.core.management.base import BaseCommand, CommandError
from app.info import *

class Command(BaseCommand):
    help = 'Get Info About Kevin Application'
    available = [
        "info"
    ]

    def add_arguments(self, parser):
        parser.add_argument('command', type=str, help='Available commands are %s' % ", ".join(self.available))

    def handle(self, *args, **options):
        # print(dir(self.style))
        if options['command'] == "info":
            self.stdout.write(self.style.SUCCESS('Current Version is: %s' % VERSION))
        else:
            raise CommandError('Command Does not exist! Please use one of the following: python manage.py kevin [%s]' % ", ".join(self.available))