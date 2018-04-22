"""
Kevin Info Command

see https://docs.djangoproject.com/en/2.0/howto/custom-management-commands/
"""
from django.core.management import utils
from django.core.management.base import BaseCommand, CommandError
from app.settings.info import *
import os

class Command(BaseCommand):
    help = 'Get Info About Kevin Application'
    available = [
        "info",
        "update_app_key"
    ]

    def add_arguments(self, parser):
        """Config Command Args"""
        parser.add_argument('command', type=str, help='Available commands are %s' % ", ".join(self.available))


    def handle(self, *args, **options):
        """Command Handle"""
        # print(dir(self.style))
        print("\n")
        if options['command'] == "info":
            self.stdout.write(self.style.SUCCESS('Current Version is: %s' % VERSION))
        elif options['command'] == "update_app_key":
            self._refresh_app_key()
        else:
            raise CommandError('Command Does not exist! Please use one of the following: python manage.py kevin [%s]' % ", ".join(self.available))
        print("\n")


    def _refresh_app_key(self):
        """Refresh APP Key"""
        if not os.path.isfile(os.path.join(APP_ROOT,'.env')):
            self.stdout.write(self.style.ERROR('Error! .env File is Missing.'))
            return None

        with open(os.path.join(APP_ROOT,'.env'), 'r') as file:
            data = file.readlines()

        i = 0
        for value in data:
            if value.startswith("APP_KEY="):
                key = utils.get_random_secret_key()
                self.stdout.write(self.style.SUCCESS('App Key Updated to: %s' % key))
                data[i] = "APP_KEY=%s\n" % key
            i += 1

        with open(os.path.join(APP_ROOT,'.env'), 'w') as file:
            file.writelines( data )