# Generated by Django 2.1.3 on 2019-04-05 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='objetivos',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='objetivos',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
