# Generated by Django 2.0.5 on 2018-05-25 19:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20180525_1919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteuser',
            name='user',
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='SiteUser',
        ),
    ]
