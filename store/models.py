from django.db import models

class BaseStore (models.Model):
    name=models.CharField(max_length=350, verbose_name='название')
    email=models.EmailField(unique=True, verbose_name='email')
    country=models.CharField(max_length=150, verbose_name='страна')
    city=models.CharField(max_length=150, verbose_name='город')
    street=models.CharField(max_length=150, verbose_name='улица')
    house_number=models.CharField(max_length=50, verbose_name='номер дома')
    time_create=models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    credit=models.DecimalField(max_digits=15, decimal_places=2, default=0, verbose_name='задолженность')

    class Meta:
        abstract = True

class Factory (BaseStore):
    """Завод"""

    def __str__(self):
        return f' {self.name}'

    class Meta:
        verbose_name = 'завод'
        verbose_name_plural = 'заводы'

class Retail:
    """Розничная сеть"""
    suppliers=models.ForeignKey(Factory, on_delete=models.CASCADE, verbose_name='поставщики')

    def __str__(self):
        return f' {self.name}'

    class Meta:
        verbose_name = 'розничная сеть'
        verbose_name_plural = 'розничные сети'

class