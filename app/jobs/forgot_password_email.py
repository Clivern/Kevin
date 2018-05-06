"""
Forgot Password Job
"""

from app.jobs.base import Base
from django.core.mail import send_mail

class Forgot_Password_Email(Base):

    _subject = None
    _message = None
    _from_email = None
    _recipient_list = []
    _fail_silently=False

    def execute(self):

        if "subject" in self._arguments and self._arguments["subject"].strip() != "":
            self._subject = self._arguments["subject"]
        else:
            self._logger.debug("Subject is Missing!")
            return False

        if "message" in self._arguments and self._arguments["message"].strip() != "":
            self._message = self._arguments["message"]
        else:
            self._logger.debug("Message is Missing!")
            return False

        if "from_email" in self._arguments and self._arguments["from_email"].strip() != "":
            self._from_email = self._arguments["from_email"]
        else:
            self._logger.debug("From Email is Missing!")
            return False

        if "recipient_list" in self._arguments and len(self._arguments["recipient_list"]) > 0:
            self._recipient_list = self._arguments["recipient_list"]
        else:
            self._logger.debug("Recipient List is Missing!")
            return False

        if "fail_silently" in self._arguments:
            self._fail_silently = self._arguments["fail_silently"]

        try:
            send_mail(
                self._subject,
                self._message,
                self._from_email,
                self._recipient_list,
                fail_silently=self._fail_silently,
            )
            return True
        except Exception as e:
            self._logger.error("Error while sending email: %s" % (e))
            return False