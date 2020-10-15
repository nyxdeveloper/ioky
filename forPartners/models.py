from django.db import models


class Document(models.Model):
    file = models.FileField('Документ', upload_to='documents')
    name = models.CharField('Название документа', max_length=150)
    filename = models.CharField('Имя файла', max_length=150, default=name)
    public = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class Info(models.Model):
    mainInfo = models.TextField('Главная информация')
    additionalInfo = models.TextField('Дополнительная информация')
    documents = models.ManyToManyField(Document, verbose_name='Документы')

    def __str__(self):
        return self.mainInfo

    class Meta:
        verbose_name = 'Инфоблок'
        verbose_name_plural = 'Инфоблоки'


class Partner(models.Model):
    firstName = models.CharField('Имя', max_length=50)
    lastName = models.CharField('Фамилия', max_length=50)
    companyName = models.CharField('Название организации', max_length=150)
    Email = models.EmailField('Email')
    message = models.TextField('Сообщение')

    def __str__(self):
        return self.companyName

    class Meta:
        verbose_name = 'Партнёр'
        verbose_name_plural = 'Партнёры'
