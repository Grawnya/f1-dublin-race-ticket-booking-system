# Generated by Django 3.2.16 on 2023-01-20 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_auto_20230120_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='for_self',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
