# Generated by Django 5.1.7 on 2025-03-19 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arbuz', '0002_alter_forms_options_alter_news_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='current_amount',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='project',
            name='target_amount',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
