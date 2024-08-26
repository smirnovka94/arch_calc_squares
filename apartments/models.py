from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Section(models.Model):
    name = models.TextField(max_length=100, verbose_name='Название секции')
    number = models.IntegerField(default=1, verbose_name='Количество этажей')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Секция'
        verbose_name_plural = 'Секции'


class Apartment(models.Model):
    type = models.TextField(max_length=10, verbose_name='Тип квартиры')
    number = models.IntegerField(default=1, verbose_name='Номер квартиры в секции')
    small_square = models.FloatField(default=1, verbose_name='Площадь без летних')
    shortened_square = models.FloatField(default=1, verbose_name='Площадь с понижающими коэф.', **NULLABLE)
    full_square = models.FloatField(default=1, verbose_name='Площадь с летними', **NULLABLE)
    Section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name='Секция')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'
