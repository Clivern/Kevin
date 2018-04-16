"""
Option Entity Module
"""
from app.models import Option

class Option_Entity():


    def insert_one(self, option):
        """Insert a New Option"""
        option = Option(
            key=option["key"],
            value=option["value"],
            autoload=option["autoload"] if "autoload" in option else "off"
        )
        option.save()
        return False if option.pk is None else option


    def insert_many(self, options):
        """Insert Many Options"""
        status = True
        for option in options:
            status &= True if self.insert_one(option) != False else False
        return status


    def get_one_by_id(self, id):
        """Get Option By ID"""
        try:
            option = Option.objects.get(pk=id)
            return False if option.pk is None else option
        except:
            return False


    def get_one_by_key(self, key):
        """Get Option By Key"""
        try:
            option = Option.objects.get(key=key)
            return False if option.pk is None else option
        except:
            return False


    def get_many_by_autoload(self, autoload):
        """Get Many Options By Autoload"""
        options = Option.objects.filter(autoload=autoload)
        return options


    def update_value_by_id(self, id, value):
        """Update Option Value By ID"""
        option = self.get_one_by_id(id)
        if option != False:
            option.value = value
            option.save()
            return True
        return False


    def update_value_by_key(self, key, value):
        """Update Option Value By Key"""
        option = self.get_one_by_key(key)
        if option != False:
            option.value = value
            option.save()
            return True
        return False


    def delete_one_by_id(self, id):
        """Delete Option By ID"""
        option = self.get_one_by_id(id)
        if option != False:
            count, deleted = option.delete()
            return True if count > 0 else False
        return False


    def delete_one_by_key(self, key):
        """Delete Option By Key"""
        option = self.get_one_by_key(key)
        if option != False:
            count, deleted = option.delete()
            return True if count > 0 else False
        return False