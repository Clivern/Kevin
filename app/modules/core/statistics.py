"""
Statistics Module
"""

from app.modules.util.helpers import Helpers
from app.modules.entity.namespace_entity import Namespace_Entity
from django.utils import timezone
from datetime import date, timedelta


class NamespacesStatistics():

    __helpers = Helpers()
    __logger = None
    __namespace_entity = Namespace_Entity()


    def __init__(self):
        self.__logger = self.__helpers.get_logger(__name__)


    def overall_count_chart(self, user_id = None):
        public_count = self.__namespace_entity.count_by_visibility(True, user_id)
        private_count = self.__namespace_entity.count_by_visibility(False, user_id)
        total_count = public_count + private_count

        if total_count > 0:
            public_percent = round((public_count / total_count) * 100)
            private_percent = round((private_count / total_count) * 100)
        else:
            public_percent = 0
            private_percent = 0

        return {
            "public": public_percent,
            "private": private_percent
        }


    def count_over_time_chart(self, days_num, user_id = None):
        data = {
            "public": self.__namespace_entity.count_by_visibility_date(True, str(days_num), user_id),
            "private": self.__namespace_entity.count_by_visibility_date(False, str(days_num), user_id),
            "public_list":{},
            "private_list":{},
            "final": {
                "public": [],
                "private": [],
                "total": []
            }
        }

        for item in data["public"]:
            data["public_list"][str(item.count_date)] = item.id

        for item in data["private"]:
            data["private_list"][str(item.count_date)] = item.id

        days_count = days_num

        while days_count > -1:
            current_date = timezone.now().date() - timedelta(days_count)
            current_date = str(current_date)

            if current_date in data["public_list"]:
                current_public = data["public_list"][current_date]
                data["final"]["public"].append(current_public)
            else:
                current_public = 0
                data["final"]["public"].append(current_public)

            if current_date in data["private_list"]:
                current_private = data["private_list"][current_date]
                data["final"]["private"].append(current_private)
            else:
                current_private = 0
                data["final"]["private"].append(current_private)

            data["final"]["total"].append(current_private + current_public)

            days_count -= 1

        data["final"]["private"] = ",".join(str(x) for x in data["final"]["private"])
        data["final"]["public"] = ",".join(str(x) for x in data["final"]["public"])
        data["final"]["total"] = ",".join(str(x) for x in data["final"]["total"])

        return {
            "private": data["final"]["private"],
            "public": data["final"]["public"],
            "total": data["final"]["total"]
        }



class EndpointsStatistics():
    pass
