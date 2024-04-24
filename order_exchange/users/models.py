from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя."""

    class Role(models.TextChoices):
        """Возможные роли пользователей."""

        CUSTOMER = 'customer', 'Заказчик'
        EXECUTOR = 'executor', 'Исполнитель'
        GUEST = 'guest', 'Гость'

    role = models.CharField(
        verbose_name='Роль',
        choices=Role.choices,
        max_length=20,
        default=Role.GUEST,
    )
    contact_details = models.TextField(
        verbose_name='Контактные данные',
        help_text='Введите ваши контактные данные.',
        max_length=200,
        blank=True,
    )
    photo = models.ImageField(
        verbose_name='Фотография',
        upload_to='posts_images',
        blank=True,
        null=True
    )
    name = models.CharField(
        verbose_name='Имя',
        max_length=20,
        blank=True,
    )

    @property
    def is_customer(self):
        return self.role == 'customer'

    @property
    def is_executor(self):
        return self.role == 'executor'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    def __str__(self):
        return self.username
