from django.db import models

class Video(models.Model):
    video_file = models.FileField(upload_to='video/', blank=True, null=True, verbose_name='Видео')

    def __str__(self):
        return f'Видео файл'

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

class ProductImages(models.Model):
    title = models.CharField(max_length=20)
    product_images = models.ImageField(upload_to='product_images/', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фото продукта'
        verbose_name_plural = 'Фото продуктов'

class Services(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название услуги', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'


class AboutMe(models.Model):
    description = models.TextField(verbose_name='Описание', blank=True, null=True)


    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Обо мне'
        verbose_name_plural = 'Обо мне'
