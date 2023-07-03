# Generated by Django 3.1.7 on 2021-05-27 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('first_name', models.CharField(default=None, max_length=50)),
                ('last_name', models.CharField(default=None, max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], default='male', max_length=20)),
                ('dob', models.DateField(blank=True, default=None, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('student_image', models.ImageField(blank=True, null=True, upload_to='student_image')),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('is_graduated', models.BooleanField(default=False)),
                ('graduated_year', models.DateField(blank=True, null=True)),
            ],
        ),
    ]