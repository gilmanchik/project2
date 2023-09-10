from django.db import models
from django.urls import reverse


class Women(models.Model):
    title = models.CharField(
        max_length=32,
        verbose_name='Заголовок'
    )

    content = models.TextField(
        verbose_name='Текст'
    )

    photo = models.ImageField(
        upload_to='photos/%Y/%m/%d',
        verbose_name='Фото'
    )

    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания'
    )

    time_update = models.DateTimeField(
        auto_now=True,
        verbose_name='Время обновления'
    )

    is_published = models.BooleanField(
        default=True,
        verbose_name='Публикация'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
