# Generated by Django 3.1.1 on 2020-10-13 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerOrganisationArchitecture', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizes',
            name='experimentNO',
            field=models.CharField(default='', max_length=50),
        ),
    ]