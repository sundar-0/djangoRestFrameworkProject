# Generated by Django 3.1.7 on 2021-05-29 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('College', '0003_auto_20210527_1551'),
        ('Faculty', '0002_auto_20210528_1213'),
        ('Student', '0001_initial'),
        ('Program', '0003_auto_20210528_1307'),
        ('Enroll', '0005_auto_20210528_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enroll',
            name='college',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, related_name='enroll_college', to='College.college'),
        ),
        migrations.AlterField(
            model_name='enroll',
            name='faculty',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, related_name='enroll_faculty', to='Faculty.faculty'),
        ),
        migrations.AlterField(
            model_name='enroll',
            name='program',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, related_name='enroll_program', to='Program.program'),
        ),
        migrations.AlterField(
            model_name='enroll',
            name='student',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.RESTRICT, related_name='enroll_student', to='Student.student'),
        ),
    ]
