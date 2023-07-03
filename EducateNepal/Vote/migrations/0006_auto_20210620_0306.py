# Generated by Django 3.1.7 on 2021-06-19 21:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Post', '0002_auto_20210618_1448'),
        ('Vote', '0005_auto_20210620_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='down_vote_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='down_vote_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vote',
            name='post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='Post.post'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='up_vote_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='up_vote_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
