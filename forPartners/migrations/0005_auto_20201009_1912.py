# Generated by Django 3.0.7 on 2020-10-09 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forPartners', '0004_auto_20201009_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='filename',
            field=models.CharField(default=models.CharField(max_length=150, verbose_name='Название документа'), max_length=150, verbose_name='Имя файла'),
        ),
    ]
