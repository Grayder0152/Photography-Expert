# Generated by Django 3.1.6 on 2021-02-09 12:36

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210209_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='big_image',
            field=models.ImageField(upload_to=main.models.user_directory_path, verbose_name='Большое изображение'),
        ),
    ]