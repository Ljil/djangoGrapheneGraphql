from django.db import models


class Occupation(models.Model):
    name = models.CharField('Имя', max_length=200)
    company_name = models.CharField('Компания', max_length=100)
    position_name = models.CharField('Должность', max_length=100)
    hire_date = models.DateField('Дата приёма')
    fire_date = models.DateField('Дата увольнения', null=True, blank=True)
    salary = models.IntegerField('Ставка')
    fraction = models.IntegerField('Ставка %')
    base = models.IntegerField('База')
    advance = models.IntegerField('Аванс')
    by_hours = models.BooleanField('Почасовая оплата')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
