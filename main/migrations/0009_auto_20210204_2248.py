# Generated by Django 3.1.6 on 2021-02-04 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_categories_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(help_text='Название категории в нижнем регистре', unique=True),
        ),
    ]
