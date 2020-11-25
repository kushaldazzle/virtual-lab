# Generated by Django 3.1.1 on 2020-10-17 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('computerOrganisationArchitecture', '0008_delete_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experiment_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('details', models.TextField()),
                ('satisfied', models.BooleanField()),
                ('date', models.DateField(auto_now_add=True)),
                ('experiment_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='computerOrganisationArchitecture.expname')),
            ],
        ),
    ]
