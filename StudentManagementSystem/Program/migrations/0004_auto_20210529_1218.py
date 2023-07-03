# Generated by Django 3.1.7 on 2021-05-29 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Faculty', '0002_auto_20210528_1213'),
        ('Program', '0003_auto_20210528_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='faculty',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, related_name='program_faculty', to='Faculty.faculty'),
        ),
    ]