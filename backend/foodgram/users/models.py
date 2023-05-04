from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint, CheckConstraint


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
        'first_name',
        'last_name',
    ]
    email = models.EmailField(
        'email address',
        max_length=254,
        unique=True,
    )
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

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Subscribe(models.Model):
    user = models.ForeignKey(
        User,
        blank=False,
        related_name='subscriber',
        verbose_name="Подписчик",
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        User,
        blank=False,
        related_name='subscribing',
        verbose_name="Автор",
        on_delete=models.CASCADE,
    )

    # def clean(self):
    #     print(self)
    #     if self.author.id == self.user.id:
    #         raise ValidationError('Нельзя подписаться на самого себя')
    #     if (self is None):
    #         raise ValidationError('Заполните одно из полей')
    # def save(self, *args, **kwargs):
    #     self.full_clean()
    #     return super().save(*args, **kwargs)

    class Meta:
        ordering = ('-id',)
        constraints = [
            UniqueConstraint(fields=['user', 'author'],
                             name='unique_subscription'),
            CheckConstraint(check=~models.Q(user=models.F('author')),
                            name='Нельзя на себя подписаться')
        ]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
