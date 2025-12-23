from django.contrib.auth.models import AbstractUser
from django.db import models

class UserModel(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField('Имя', max_length=150)
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        verbose_name='Аватар',
    )

    REQUIRED_FIELDS = ['username', 'first_name']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username
    

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Service(models.Model):
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание', blank=True)
    image = models.ImageField(upload_to='services/', blank=True, null=True, verbose_name='Изображение')
    created_at = models.DateTimeField('Дата добавления', auto_now_add=True)
    is_active = models.BooleanField('Активен', default=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Товар/Услуга'
        verbose_name_plural = 'Товары/Услуги'
    
    def __str__(self):
        return self.name