# Generated by Django 3.1.7 on 2021-06-19 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_auto_20210618_1448'),
        ('Vote', '0006_auto_20210620_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='Post.post'),
        ),
    ]