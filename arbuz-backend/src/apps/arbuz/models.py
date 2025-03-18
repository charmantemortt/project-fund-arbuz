from datetime import date, timezone
from django.db import models
from .managers import FormsManager

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return f"{self.name}"

PAY_CHOICE = (
    ('разовый', 'разовый'),
    ('ежемесячный', 'ежемесячный')
)

LINKS_CHOICE = (
    ('да', 'да'),
    ('нет', 'нет')
)

class Forms(models.Model):
    sum = models.DecimalField(decimal_places=1, max_digits=10)
    pay_status = models.CharField(max_length=100, choices=PAY_CHOICE)
    user_name = models.CharField(max_length=255)
    comment = models.TextField()
    link_status = models.CharField(max_length=500, choices=LINKS_CHOICE)
    link_field = models.TextField()

    objects = FormsManager()

    def __str__(self):
        return f"{self.sum}"

class News(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(blank=False, null=True, auto_now=True)

    def __str__(self):
        return f"{self.name}"