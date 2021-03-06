# Generated by Django 3.1.6 on 2021-02-04 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210204_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='images',
        ),
        migrations.RemoveField(
            model_name='images',
            name='image',
        ),
        migrations.AddField(
            model_name='images',
            name='big_image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Большое изображение'),
        ),
        migrations.AddField(
            model_name='images',
            name='small_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Маленькое изображение'),
        ),
        migrations.AlterField(
            model_name='images',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.categories', verbose_name='Категория фотографии'),
        ),
    ]
