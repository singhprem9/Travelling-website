# Generated by Django 4.0 on 2022-02-15 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_bookings_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='phone',
            field=models.IntegerField(verbose_name='NULL'),
        ),
    ]
