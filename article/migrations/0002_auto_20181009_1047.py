# Generated by Django 2.1.1 on 2018-10-09 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('title',), 'verbose_name': 'Раздел', 'verbose_name_plural': 'Разделы'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ('title',), 'verbose_name': 'Метка', 'verbose_name_plural': 'Метки'},
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=50, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=50, unique=True, verbose_name='Тег'),
        ),
    ]