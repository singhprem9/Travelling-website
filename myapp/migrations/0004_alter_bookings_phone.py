# Generated by Django 4.0 on 2022-02-15 14:49

from django.db import migrations, models
import unicodedata


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_bookings_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='phone',
            field=models.IntegerField(default=unicodedata.numeric),
        ),
    ]
