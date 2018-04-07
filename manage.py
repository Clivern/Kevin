#!/usr/bin/env python
import os
import sys

__author__ = "Clivern"
__copyright__ = "Copyright 2018, Clivern"
__license__ = "Apache Version 2.0"
__version__ = "1.0.0"
__maintainer__ = "A. F"
__email__ = "hello@clivern.com"
__status__ = "production"


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings." + __status__)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
