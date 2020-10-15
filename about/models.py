from django.db import models


class StoryGalleryPhoto(models.Model):
    photo = models.ImageField('Фото', upload_to='storyGalleryPhotos')
    name = models.CharField('Название', max_length=100, null=True, default='')

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.id

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'


class Phone(models.Model):
    name = models.CharField('Имя', max_length=50)
    number = models.CharField('Номер', max_length=17)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Номер телефона'
        verbose_name_plural = 'Номера телефонов'


class TeamMember(models.Model):
    firstName = models.CharField('Имя', max_length=50)
    lastName = models.CharField('Фамилия', max_length=50)
    position = models.CharField('Должность', max_length=150)
    phoneNumber = models.ManyToManyField(Phone, verbose_name='Телефон', null=True, default=None)
    about = models.TextField('О человеке (вкратце)')
    yearOfAccesion = models.SmallIntegerField('В каком году пришёл')
    photo = models.ImageField('Фото', upload_to='team')

    def __str__(self):
        return self.firstName + ' ' + self.lastName

    class Meta:
        verbose_name = 'Член команды'
        verbose_name_plural = 'Члены команды'


class Story(models.Model):
    title = models.CharField('Заголовок', max_length=200, default='')
    description = models.TextField('Описание', default='')
    photo = models.ImageField('Фото', upload_to='storyPhotos', null=True)
    gallery = models.ManyToManyField(StoryGalleryPhoto, verbose_name='Галлерея', null=True)
    video = models.FileField('Видео', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'


class Partner(models.Model):
    name = models.CharField('Компания', max_length=150, default='')
    logo = models.ImageField('Логотип', upload_to='partners', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Партнёр'
        verbose_name_plural = 'Партнёры'
