from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Section(models.Model):
    name = models.TextField(max_length=100, default="Секция ", verbose_name='Название секции')
    number = models.IntegerField(default=1, verbose_name='Количество этажей')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Секция'
        verbose_name_plural = 'Секции'


class Apartment(models.Model):
    TYPES = [
        ("s", "Студии"),
        ("1kk", "1-комнатные"),
        ("2kk", "2-комнатные"),
        ("3kk", "3-комнатные")
    ]

    type = models.TextField(max_length=10, choices=TYPES, default="1kk", verbose_name='Тип квартиры')
    number = models.IntegerField(default=1, verbose_name='Номер квартиры в секции')
    small_square = models.FloatField(default=1, verbose_name='Площадь без летних')
    shortened_square = models.FloatField(default=1, verbose_name='Площадь с понижающими коэф.', **NULLABLE)
    full_square = models.FloatField(default=1, verbose_name='Площадь с летними', **NULLABLE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name='Секция')

    def __str__(self):
        return f"{self.type} - {self.small_square}"

    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'
