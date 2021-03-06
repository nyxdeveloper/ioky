# Generated by Django 3.0.7 on 2020-10-15 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_teammember_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('number', models.CharField(max_length=13, verbose_name='Номер')),
            ],
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='phoneNumber',
        ),
        migrations.AddField(
            model_name='teammember',
            name='phoneNumber',
            field=models.ManyToManyField(default=None, null=True, to='about.Phone', verbose_name='Телефон'),
        ),
    ]
