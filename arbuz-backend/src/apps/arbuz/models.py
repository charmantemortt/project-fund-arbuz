from datetime import date, timezone
from django.db import models

class Projects(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name

# CHOICE = (
#     ('', ''),
#     ('', '')
# )
#
# # class Forms(models.Model):
# #     user_name = models.CharField(max_length=255)
# #     status = models.CharField(max_length=100, choices=CHOICE)
# #
# #
# # class News(models.Model):
# #     name = models.CharField(max_length=255)
# #     description = models.TextField()
# #     created_at = models.DateTimeField(default=timezone.now)
