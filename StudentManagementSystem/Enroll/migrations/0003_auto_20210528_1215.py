# Generated by Django 3.1.7 on 2021-05-28 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
        ('Enroll', '0002_auto_20210528_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enroll',
            name='student',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='Student.student'),
        ),
    ]
