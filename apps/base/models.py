from django.db import models

# Create your models here.

class Index(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок сайта", 
        blank=True, null=True
    )
    description = models.TextField(
        max_length=255,
        verbose_name="Описание сайта", 
        blank=True, null=True
    )
    logo = models.ImageField(
        upload_to='image/',
        verbose_name="Логотип сайта"
    )
    