from django.db import models


class Question(models.Model):
    question = models.TextField('Вопрос')
    answer = models.TextField('Ответ', blank=True)
    name = models.CharField('Имя спросившего', max_length=150, null=True, blank=True, default='Incognito')
    Email = models.EmailField('Почта спросившего', null=True, blank=True)
    check = models.BooleanField('В проверке/Проверено', default=False)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.question
