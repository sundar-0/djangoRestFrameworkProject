# Generated by Django 3.1.7 on 2021-05-27 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Faculty', '0001_initial'),
        ('Program', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('college_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('college_name', models.CharField(default=None, max_length=200)),
                ('college_location', models.CharField(default=None, max_length=200)),
                ('faculty', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Faculty.faculty')),
                ('program', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Program.program')),
            ],
        ),
    ]
