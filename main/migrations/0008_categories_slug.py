# Generated by Django 3.1.6 on 2021-02-04 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210204_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='slug',
            field=models.SlugField(default='<django.db.models.fields.charfield>', help_text='Название категории в нижнем регистре', unique=True),
        ),
    ]
