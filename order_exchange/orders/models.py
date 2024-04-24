from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

USER = get_user_model()


class Order(models.Model):
    name = models.CharField(
        verbose_name='Наименование',
        max_length=150,
    )
    description = models.TextField(
        verbose_name='Описание заказа',
        max_length=200,
    )
    value = models.IntegerField(verbose_name='Стоимость заказа')
    customer = models.ForeignKey(
        USER,
        verbose_name='Заказчик',
        on_delete=models.CASCADE,
        related_name='customer_orders',
    )
    executor = models.ForeignKey(
        USER,
        verbose_name='Исполнитель',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='executor_orders',
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['created_at']

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('orders:order_detail', kwargs={'order_id': self.pk})
