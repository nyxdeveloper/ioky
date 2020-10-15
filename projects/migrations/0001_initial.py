# Generated by Django 3.0.7 on 2020-09-29 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название проекта')),
                ('shortDescription', models.TextField(verbose_name='Короткое описание проекта')),
                ('description', models.TextField(verbose_name='Описание проекта')),
                ('image', models.ImageField(upload_to='projects', verbose_name='Картинка')),
            ],
        ),
    ]
