from datetime import date, timezone
from django.db import models

class Projects(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return f"{self.name}"

PAY_CHOICE = (
    ('разовый', "разовый"),
    ('ежемесячный', "ежемесячный")
)

LINKS_CHOICE = (
    ('да', 'да'),
    ('нет', 'нет')
)

class Forms(models.Model):
    summa = models.DecimalField(decimal_places=1, max_digits=100000)
    pay_status = models.CharField(max_length=100, choices=PAY_CHOICE)
    user_name = models.CharField(max_length=255)
    comment = models.TextField()
    link_status = models.CharField(max_length=500, choices=LINKS_CHOICE)
    link_field = models.TextField()

    def __str__(self):
        return f"{self.summa}"

class News(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(blank=False, null=True, default=timezone.now)

    def __str__(self):
        return f"{self.name}"