from django.db import models


def user_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.category.__str__(), filename)


class Categories(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название категории', unique=True)
    slug = models.SlugField(unique=True, help_text='Название категории в нижнем регистре')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"
        ordering = ['id']


class Images(models.Model):
    category = models.ForeignKey(Categories, verbose_name='Категория фотографии', on_delete=models.CASCADE)
    big_image = models.ImageField(verbose_name='Большое изображение', upload_to=user_directory_path)
    small_image = models.ImageField(verbose_name='Маленькое изображение', null=True, blank=True,
                                    upload_to=user_directory_path,
                                    help_text='Это поле не обязательное')

    def __str__(self):
        return f'{self.category}-{self.id}'

    class Meta:
        verbose_name = "Фотографию"
        verbose_name_plural = "Фотографии"
