# Generated by Django 3.2.15 on 2023-04-30 09:56

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0002_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='recipes/', verbose_name='Изображение')),
                ('cooking_time', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1, message='Минимальное значение 1!')], verbose_name='Время приготовления')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recipes', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('tags', models.ManyToManyField(related_name='recipes', to='recipes.Tag', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
                'ordering': ('-id',),
            },
        ),
    ]
