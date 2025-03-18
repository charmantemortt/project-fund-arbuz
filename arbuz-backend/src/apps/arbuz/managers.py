from django.db import models

class FormsManager(models.Manager):
    def create_form(self, data):
        form = self.create(
            sum = data["sum"],
            pay_status = data["pay_status"],
            user_name= data["user_name"],
            comment= data["comment"],
            link_status= data["link_status"],
            link_field= data["link_field"]
        )
