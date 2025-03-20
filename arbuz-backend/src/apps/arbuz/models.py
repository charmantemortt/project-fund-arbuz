from django.db import models
from .managers import FormsManager

class Project(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    current_amount = models.DecimalField(decimal_places=1, max_digits=10, default=0, verbose_name='Текущий сбор')
    target_amount = models.DecimalField(decimal_places=1, max_digits=10, verbose_name='Цель сборов')
    image = models.ImageField(verbose_name='Изображение')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

PAY_CHOICE = (
    ('разовый', 'разовый'),
    ('ежемесячный', 'ежемесячный')
)

LINKS_CHOICE = (
    ('да', 'да'),
    ('нет', 'нет')
)

class Forms(models.Model):
    sum = models.DecimalField(decimal_places=1, max_digits=10, verbose_name='Сумма для отправки')
    pay_status = models.CharField(max_length=100, choices=PAY_CHOICE, verbose_name='Выбор платежа')
    user_name = models.CharField(max_length=255, verbose_name='Имя отправителя')
    comment = models.TextField(verbose_name='Комментарий')
    link_status = models.CharField(max_length=500, choices=LINKS_CHOICE, verbose_name='Выбор отправителя')
    link_field = models.TextField(verbose_name='Ссылка')

    objects = FormsManager()

    def __str__(self):
        return f"{self.user_name}, {self.sum}"

    class Meta:
        verbose_name = 'Форма'
        verbose_name_plural = 'Формы'

class News(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(blank=False, null=True, auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'