# Generated by Django 3.2.16 on 2023-01-18 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20230118_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='for_self',
            field=models.BooleanField(default=True),
        ),
    ]
