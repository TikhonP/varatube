# Generated by Django 3.0.4 on 2020-04-08 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='file',
            field=models.FileField(upload_to='videos/%Y/%m/%d', verbose_name='Видео'),
        ),
    ]
