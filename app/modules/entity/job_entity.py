"""
Job Entity Module
"""

from app.models import Job

class Job_Entity():

    ONCE = "once"
    ONCE_AT_TS = "once_at_%s"
    EVERY_X_SEC = "every_%s_sec"
    EVERY_X_MIN = "every_%s_min"
    EVERY_X_HOUR = "every_%s_hour"
    EVERY_X_DAY = "every_%s_day"
    EVERY_X_WEEK = "every_%s_week"
    EVERY_X_MONTH = "every_%s_month"
    EVERY_X_YEAR = "every_%s_year"