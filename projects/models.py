from django.db import models


class ProjectModel(models.Model):
    name = models.CharField('Модель', max_length=150)
    V = models.FloatField('Выходное напряжение')
    I = models.FloatField('Сила тока')
    appointment = models.CharField('Назначение', max_length=150)
    size = models.CharField('Размер', max_length=150)
    term = models.FloatField('Срок работы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'


class Project(models.Model):
    title = models.CharField('Название проекта', max_length=150)
    shortDescription = models.TextField('Короткое описание проекта')
    description = models.TextField('Описание проекта')
    image = models.ImageField('Картинка', upload_to='projects')
    slug = models.SlugField('URL', max_length=50, unique=True)
    projectModels = models.ManyToManyField(ProjectModel, verbose_name='Модели', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
