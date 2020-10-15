# Generated by Django 3.0.7 on 2020-10-05 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='documents', verbose_name='Документ')),
                ('name', models.CharField(max_length=150, verbose_name='Название документа')),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainInfo', models.TextField(verbose_name='Главная информация')),
                ('additionalInfo', models.TextField(verbose_name='Дополнительная информация')),
                ('documents', models.ManyToManyField(to='forPartners.Document', verbose_name='Документы')),
            ],
        ),
    ]
