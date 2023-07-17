
from django.db import models


class Tags(models.Model):
    name = models.CharField(max_length=60, verbose_name='Название')

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    # tag = models.ManyToManyField(Tags, related_name='articles')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class ArticleTagsPositions(models.Model):
    article = models.ForeignKey(Article, related_name='positions', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, related_name='positions', on_delete=models.CASCADE)
    is_main = models.BooleanField()
