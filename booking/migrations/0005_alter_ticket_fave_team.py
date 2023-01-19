# Generated by Django 3.2.16 on 2023-01-19 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_alter_ticket_for_self'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='fave_team',
            field=models.IntegerField(choices=[('red_bull', 'Red Bull'), ('ferrari', 'Ferrari'), ('mercedes', 'Mercedes'), ('alpine', 'Alpine'), ('mclaren', 'McLaren'), ('alfa_romeo', 'Alfa Romeo'), ('aston_martin', 'Aston Martin'), ('haas', 'Haas'), ('alphatauri', 'AlphaTauri'), ('williams', 'Williams')], default='Red Bull'),
        ),
    ]
