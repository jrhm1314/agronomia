# Generated by Django 2.1.3 on 2019-03-28 20:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190328_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]