# Generated by Django 2.1.3 on 2019-03-28 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0020_auto_20190327_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='img_edu',
            field=models.ImageField(blank=True, null=True, upload_to='educacion'),
        ),
        migrations.AddField(
            model_name='profile',
            name='img_exp',
            field=models.ImageField(blank=True, null=True, upload_to='experiencia'),
        ),
        migrations.AddField(
            model_name='profile',
            name='img_hab',
            field=models.ImageField(blank=True, null=True, upload_to='habilidades'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='estatus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Estatus', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='upload',
            field=models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='Documento'),
        ),
    ]
