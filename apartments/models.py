from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Apartment(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название квартиры')
    number = models.IntegerField(default=1, verbose_name='Номер квартиры в секции')
    type = models.TextField(max_length=10, verbose_name='Тип квартиры')
    small_square  = models.FloatField(default=1, verbose_name='Площадь без летних')
    shortened_square = models.FloatField(default=1, verbose_name='Площадь с понижающими коэф.', **NULLABLE)
    full_square = models.FloatField(default=1, verbose_name='Площадь с летними', **NULLABLE)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'
