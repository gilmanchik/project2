from django.db import models
from django.urls import reverse


class Women(models.Model):
    title = models.CharField(
        max_length=32,
        verbose_name='Заголовок'
    )

    slug = models.SlugField(
        max_length=32,
        unique=True,
        db_index=True,
        verbose_name='URL'
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

    cat = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Женщины'
        verbose_name_plural = 'Женщины'
        ordering = ['-time_create', 'title']


class Category(models.Model):
    name = models.CharField(
        max_length=32,
        db_index=True,
        verbose_name='Название'
    )

    slug = models.SlugField(
        max_length=32,
        unique=True,
        db_index=True,
        verbose_name='URL'
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
