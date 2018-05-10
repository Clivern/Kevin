"""
Forgot Password Job
"""

# Django
from django.core.mail import send_mail
from django.utils.translation import gettext as _
from django.template.loader import render_to_string

# local Django
from app.jobs.base import Base


class Forgot_Password_Email(Base):

    _data = {}
    _subject = _("%s Password Reset")
    _template = "mails/reset_password.html"


    def execute(self):

        if "app_name" not in self._arguments or "app_email" not in self._arguments or "app_url" not in self._arguments:
            self._logger.error("App name or app email or app url is missing!")
            return False

        if "recipient_list" not in self._arguments or len(self._arguments["recipient_list"]) < 1:
            self._logger.error("Recipient List is Missing!")
            return False

        if "token" not in self._arguments or self._arguments["token"].strip() == "":
            self._logger.error("Reset Token is Missing!")
            return False

        if "fail_silently" not in self._arguments:
            self._arguments["fail_silently"] = False

        self._subject = self._subject % (self._arguments["app_name"])

        self._data = {
            "app_name": self._arguments["app_name"],
            "email_title": self._subject,
            "app_url": self._arguments["app_url"],
            "token": self._arguments["token"]
        }

        try:
            send_mail(
                self._subject,
                "",
                self._arguments["app_email"],
                self._arguments["recipient_list"],
                fail_silently=self._arguments["fail_silently"],
                html_message=self._get_message()
            )
            return True
        except Exception as e:
            self._logger.error("Error while sending email: %s" % (e))
            return False


    def _get_message(self):
         return render_to_string(self._template, self._data)