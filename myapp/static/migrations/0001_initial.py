# Generated by Django 4.0 on 2022-02-02 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Travels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Place', models.CharField(max_length=50)),
                ('description', models.CharField(default='', max_length=400)),
                ('image', models.ImageField(upload_to='uploads/Tours/')),
            ],
        ),
    ]