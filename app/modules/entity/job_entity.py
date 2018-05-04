"""
Job Entity Module
"""

from app.models import Job
from django.utils import timezone
from datetime import timedelta
import json

class Job_Entity():

    ONCE = "once"
    ONCE_AT = "once_at"
    EVERY = "every"

    def insert_one(self, job):
        """Insert a New Job"""
        job = Job(
            name=job["name"],
            status=job["status"] if "status" in job else "pending",
            executor=job["executor"],
            parameters=job["parameters"],
            interval=json.dumps(job["interval"]),
            retry_count=job["retry_count"] if "retry_count" in job else 0,
            priority=job["priority"] if "priority" in job else 1,
            run_at=job["run_at"] if "run_at" in job else None,
            last_run=job["last_run"] if "last_run" in job else self._get_run_at(job["interval"])
        )

        job.save()
        return False if job.pk is None else job

    def insert_many(self, jobs):
        """Insert Many Jobs"""
        status = True
        for job in jobs:
            status &= True if self.insert_one(job) != False else False
        return status

    def get_one_by_id(self, id):
        """Get Job By ID"""
        try:
            job = Job.objects.get(pk=id)
            return False if job.pk is None else job
        except:
            return False

    def delete_one_by_id(self, id):
        """Delete Job By ID"""
        job = self.get_one_by_id(id)
        if job != False:
            count, deleted = job.delete()
            return True if count > 0 else False
        return False

    def _get_run_at(self, interval):
        """Get Run at Datetime"""
        if interval["type"] == Job_Entity.ONCE:
            return timezone.now()

        if interval["type"] == Job_Entity.ONCE_AT:
            return interval["datetime"]

        if interval["type"] == Job_Entity.EVERY:
            datetime = timezone.now()
            for key, value in interval.items():
                if key == "microseconds":
                    datetime += timedelta(microseconds=value)
                elif key == "milliseconds":
                    datetime += timedelta(milliseconds=value)
                elif key == "seconds":
                    datetime += timedelta(seconds=value)
                elif key == "minutes":
                    datetime += timedelta(minutes=value)
                elif key == "hours":
                    datetime += timedelta(hours=value)
                elif key == "days":
                    datetime += timedelta(days=value)
                elif key == "weeks":
                    datetime += timedelta(weeks=value)
            return datetime