from datetime import date, timezone
from django.db import models

class Projects(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name