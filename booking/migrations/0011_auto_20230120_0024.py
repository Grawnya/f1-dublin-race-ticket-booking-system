# Generated by Django 3.2.16 on 2023-01-20 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_auto_20230120_0009'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seat',
            options={'ordering': ['stand', 'seat_number']},
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='row',
        ),
        migrations.AlterUniqueTogether(
            name='seat',
            unique_together={('stand', 'seat_number')},
        ),
        migrations.RemoveField(
            model_name='seat',
            name='row',
        ),
    ]