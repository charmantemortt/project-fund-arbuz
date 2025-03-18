from django.db import models

class FormsManager(models.Manager):
    def create_form(self, sum, pay_status, user_name, comment, link_status, link_field):
        form = self.create(
            sum = sum,
            pay_status = pay_status,
            user_name=user_name,
            comment=comment,
            link_status=link_status,
            link_field=link_field
        )
        print(f"Заявка создана: {form}")
        return form
