# Generated by Django 2.0.3 on 2018-03-25 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='descriptor',
            field=models.TextField(default=None, verbose_name='Дескриптор'),
        ),
    ]
