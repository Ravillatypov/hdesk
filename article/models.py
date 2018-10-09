from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    '''
    Класс категорий статей
    '''
    title = models.CharField('Название', max_length=50, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.title


class Tag(models.Model):
    '''
    Класс тегов статей
    '''
    title = models.CharField('Тег', max_length=50, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Метка'
        verbose_name_plural = 'Метки'
    
    def __str__(self):
        return self.title


class Article(models.Model):
    '''
    Класс статей
    '''
    created = models.DateTimeField('Дата создания', 'created_at', False, True, editable=False)
    updated = models.DateTimeField('Дата изменения', 'updated_at', True, editable=False)
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор', editable=False)
    title = models.CharField(max_length=170, verbose_name='Название статьи', unique=True)
    text = models.TextField('Текст статьи', 'post')
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(Tag, verbose_name='Теги', blank=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class Comment(models.Model):
    '''
    Класс комментарий к статье
    '''
    created = models.DateTimeField('Дата создания', 'created_at', False, True, editable=False)
    updated = models.DateTimeField('Дата изменения', 'updated_at', True, editable=False)
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор', editable=False)
    text = models.TextField('Комментарии', 'comment')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
    
    def __str__(self):
        return '{s.author}'.format(s=self)
