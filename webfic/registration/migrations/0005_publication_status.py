# Generated by Django 2.1.3 on 2019-03-08 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20190308_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='status',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Estatus'),
        ),
    ]
