# Generated by Django 3.1.2 on 2020-11-30 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
