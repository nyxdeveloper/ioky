# Generated by Django 3.0.7 on 2020-10-02 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='Вопрос')),
                ('answer', models.TextField(blank=True, verbose_name='Ответ')),
                ('name', models.CharField(blank=True, default='Incognito', max_length=150, verbose_name='Имя спросившего')),
                ('Email', models.EmailField(blank=True, max_length=254, verbose_name='Почта спросившего')),
                ('check', models.BooleanField(verbose_name='В проверке/Проверено')),
            ],
        ),
        migrations.DeleteModel(
            name='Carousel',
        ),
    ]