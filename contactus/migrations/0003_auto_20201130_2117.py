# Generated by Django 3.1.2 on 2020-11-30 15:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0002_contactus_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='message',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactus',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='name',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='phone',
            field=models.CharField(default='', max_length=13),
        ),
    ]
