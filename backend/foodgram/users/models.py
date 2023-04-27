from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя"""
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=150,
        blank=False
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=150,
        blank=False
    )
    email = models.EmailField(
        verbose_name='Email',
        max_length=254,
        unique=True
    )

    class Meta:
        ordering = ['-pk']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Follow(models.Model):
    """Модель подписки"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Follower',
        related_name='follower'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Following',
        related_name='following'
    )

    class Meta:

        models.UniqueConstraint(fields=['user', 'author'], name='unique')

        def __str__(self):
            return f'{self.user} подписан на {self.author}'
