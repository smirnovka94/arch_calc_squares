from django.conf import settings
from django.db import models
from django.db.models import Sum, F, Count
from django.db.models.signals import pre_save
from django.dispatch import receiver

NULLABLE = {'blank': True, 'null': True}


"""class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя проекта')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                                verbose_name='автор')

    def __str__(self):
        return self.name

    def s_count(self):
        s_count = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='s')  # Только студии
                s_count += sum(count_floor for _ in apartments)  # Учитываем количество этажей
        return s_count

    def sum_count(self):
        total_count = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor)
                total_count += sum(count_floor for _ in apartments)  # Учитываем количество этажей
        return total_count

    def sum_small_square(self):
        total_small_square = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor)
                total_small_square += sum(
                    apartment.small_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return total_small_square

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'проекты'
"""
class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя проекта')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='автор')

    def sum_count_project(self):
        sum_count = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor)
                sum_count += sum(count_floor for _ in apartments)  # Учитываем количество этажей
        return sum_count

    def sum_s_count_project(self):
        sum_count = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='s')
                sum_count += sum(count_floor for _ in apartments)  # Учитываем количество этажей
        return round(sum_count, 2)

    def sum_k_count_project(self):
        sum_count = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='1kk')
                sum_count += sum(count_floor for _ in apartments)  # Учитываем количество этажей
        return round(sum_count, 2)

    def sum_kk_count_project(self):
        sum_count = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='2kk')
                sum_count += sum(count_floor for _ in apartments)  # Учитываем количество этажей
        return round(sum_count, 2)

    def sum_kkk_count_project(self):
        sum_count = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='3kk')
                sum_count += sum(count_floor for _ in apartments)  # Учитываем количество этажей
        return round(sum_count, 2)

    def sum_kkkk_count_project(self):
        sum_count = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='4kk')
                sum_count += sum(count_floor for _ in apartments)  # Учитываем количество этажей
        return round(sum_count, 2)

    def sum_kkkkk_count_project(self):
        sum_count = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='5kk')
                sum_count += sum(count_floor for _ in apartments)  # Учитываем количество этажей
        return round(sum_count, 2)

    def sum_kkkkkk_count_project(self):
        sum_count = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='6kk')
                sum_count += sum(count_floor for _ in apartments)  # Учитываем количество этажей
        return round(sum_count, 2)

    def sum_kkkkkkk_count_project(self):
        sum_count = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='7kk')
                sum_count += sum(count_floor for _ in apartments)  # Учитываем количество этажей
        return round(sum_count, 2)

    def sum_small_square_project(self):
        total_small_square = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor)
                total_small_square += sum(
                    apartment.small_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_small_square, 2)

    def sum_s_small_square_project(self):
        total_small_square = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='s')
                total_small_square += sum(
                    apartment.small_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_small_square, 2)

    def sum_k_small_square_project(self):
        total_small_square = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='1kk')
                total_small_square += sum(
                    apartment.small_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_small_square, 2)
    
    def sum_kk_small_square_project(self):
        total_small_square = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='2kk')
                total_small_square += sum(
                    apartment.small_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_small_square, 2)
    
    def sum_kkk_small_square_project(self):
        total_small_square = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='3kk')
                total_small_square += sum(
                    apartment.small_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_small_square, 2)

    def sum_kkkk_small_square_project(self):
        total_small_square = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='4kk')
                total_small_square += sum(
                    apartment.small_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_small_square, 2)

    def sum_kkkkk_small_square_project(self):
        total_small_square = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='5kk')
                total_small_square += sum(
                    apartment.small_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_small_square, 2)

    def sum_kkkkkk_small_square_project(self):
        total_small_square = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='6kk')
                total_small_square += sum(
                    apartment.small_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_small_square, 2)

    def sum_shortened_square_project(self):
        total_shortened_square = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor)
                total_shortened_square += sum(
                    apartment.shortened_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_shortened_square, 2)

    def sum_s_shortened_square_project(self):
        total_shortened_square = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='s')
                total_shortened_square += sum(
                    apartment.shortened_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_shortened_square, 2)

    def sum_k_shortened_square_project(self):
        total_shortened_square = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='1kk')
                total_shortened_square += sum(
                    apartment.shortened_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_shortened_square, 2)

    def sum_kk_shortened_square_project(self):
        total_shortened_square = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='2kk')
                total_shortened_square += sum(
                    apartment.shortened_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_shortened_square, 2)

    def sum_kkk_shortened_square_project(self):
        total_shortened_square = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='3kk')
                total_shortened_square += sum(
                    apartment.shortened_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_shortened_square, 2)

    def sum_kkkk_shortened_square_project(self):
        total_shortened_square = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='4kk')
                total_shortened_square += sum(
                    apartment.shortened_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_shortened_square, 2)

    def sum_kkkkk_shortened_square_project(self):
        total_shortened_square = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='5kk')
                total_shortened_square += sum(
                    apartment.shortened_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_shortened_square, 2)

    def sum_kkkkkk_shortened_square_project(self):
        total_shortened_square = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='6kk')
                total_shortened_square += sum(
                    apartment.shortened_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_shortened_square, 2)

    def sum_kkkkkkk_shortened_square_project(self):
        total_shortened_square = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='7kk')
                total_shortened_square += sum(
                    apartment.shortened_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_shortened_square, 2)

    def sum_full_square_project(self):
        total_full_square = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor)
                total_full_square += sum(
                    apartment.full_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_full_square, 2)

    def sum_s_full_square_project(self):
        total_full_square = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='s')
                total_full_square += sum(
                    apartment.full_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_full_square, 2)

    def sum_k_full_square_project(self):
        total_full_square = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='1kk')
                total_full_square += sum(
                    apartment.full_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_full_square, 2)

    def sum_kk_full_square_project(self):
        total_full_square = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='2kk')
                total_full_square += sum(
                    apartment.full_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_full_square, 2)

    def sum_kkk_full_square_project(self):
        total_full_square = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='3kk')
                total_full_square += sum(
                    apartment.shortened_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_full_square, 2)

    def sum_kkkk_full_square_project(self):
        total_full_square = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='4kk')
                total_full_square += sum(
                    apartment.shortened_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_full_square, 2)

    def sum_kkkkk_full_square_project(self):
        total_full_square = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='5kk')
                total_full_square += sum(
                    apartment.shortened_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_full_square, 2)

    def sum_kkkkkk_full_square_project(self):
        total_full_square = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='6kk')
                total_full_square += sum(
                    apartment.shortened_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_full_square, 2)

    def sum_kkkkkkk_full_square_project(self):
        total_full_square = 0
        sections = Section.objects.filter(project=self)
        for section in sections:
            floors = Floor.objects.filter(section=section)
            for floor in floors:
                count_floor = floor.count_floor
                apartments = Apartment.objects.filter(floor=floor, type='7kk')
                total_full_square += sum(
                    apartment.shortened_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_full_square, 2)

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.TextField(max_length=100, default="Секция ", verbose_name='Название секции')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='sections', verbose_name='Проект')
    is_visible = models.BooleanField(default=True, verbose_name='Видимость')

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                                verbose_name='автор')

    def __str__(self):
        return self.name


    def sum_floors(self):
        # Инициализируем сумму
        total_sum_floors = 0

        # Получаем все этажи, относящиеся к секции
        floors = Floor.objects.filter(section=self)

        # Итерация по этажам и суммирование small_square квартир
        for floor in floors:
            count_floor = floor.count_floor
            total_sum_floors += count_floor

        return total_sum_floors

    def sum_count_section(self):
        sum_count = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor)
            sum_count += sum(count_floor for _ in apartments)  # Учитываем количество этажей
        return sum_count

    def sum_s_count_section(self):
        sum_count = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='s')
            sum_count += sum(count_floor for _ in apartments)  # Учитываем количество этажей
        return round(sum_count, 2)

    def sum_k_count_section(self):
        sum_count = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='1kk')
            sum_count += sum(count_floor for _ in apartments)  # Учитываем количество этажей
        return round(sum_count, 2)

    def sum_kk_count_section(self):
        sum_count = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='2kk')
            sum_count += sum(count_floor for _ in apartments)  # Учитываем количество этажей
        return round(sum_count, 2)

    def sum_kkk_count_section(self):
        sum_count = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='3kk')
            sum_count += sum(count_floor for _ in apartments)  # Учитываем количество этажей
        return round(sum_count, 2)

    def sum_kkkk_count_section(self):
        sum_count = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='4kk')
            sum_count += sum(count_floor for _ in apartments)  # Учитываем количество этажей
        return round(sum_count, 2)

    def sum_kkkkk_count_section(self):
        sum_count = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='5kk')
            sum_count += sum(count_floor for _ in apartments)  # Учитываем количество этажей
        return round(sum_count, 2)

    def sum_kkkkkk_count_section(self):
        sum_count = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='6kk')
            sum_count += sum(count_floor for _ in apartments)  # Учитываем количество этажей
        return round(sum_count, 2)

    def sum_kkkkkkk_count_section(self):
        sum_count = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='7kk')
            sum_count += sum(count_floor for _ in apartments)  # Учитываем количество этажей
        return round(sum_count, 2)

    def sum_small_square_section(self):
        # Инициализируем сумму
        total_small_square = 0

        # Получаем все этажи, относящиеся к секции
        floors = Floor.objects.filter(section=self)

        # Итерация по этажам и суммирование small_square квартир
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor)
            total_small_square += sum(apartment.small_square * count_floor for apartment in apartments)

        return round(total_small_square,2)

    def sum_s_small_square_section(self):
        total_small_square = 0

        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='s')
            total_small_square += sum(
                apartment.small_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_small_square, 2)

    def sum_k_small_square_section(self):
        total_small_square = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='1kk')
            total_small_square += sum(
                apartment.small_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_small_square, 2)

    def sum_kk_small_square_section(self):
        total_small_square = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='2kk')
            total_small_square += sum(
                apartment.small_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_small_square, 2)

    def sum_kkk_small_square_section(self):
        total_small_square = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='3kk')
            total_small_square += sum(
                apartment.small_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_small_square, 2)

    def sum_kkkk_small_square_section(self):
        total_small_square = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='4kk')
            total_small_square += sum(
                apartment.small_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_small_square, 2)

    def sum_kkkkk_small_square_section(self):
        total_small_square = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='5kk')
            total_small_square += sum(
                apartment.small_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_small_square, 2)

    def sum_kkkkkk_small_square_section(self):
        total_small_square = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='6kk')
            total_small_square += sum(
                apartment.small_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_small_square, 2)

    def sum_kkkkkkk_small_square_section(self):
        total_small_square = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='7kk')
            total_small_square += sum(
                apartment.small_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_small_square, 2)

    def sum_shortened_square_section(self):
        # Инициализируем сумму
        total_shortened_square = 0

        # Получаем все этажи, относящиеся к секции
        floors = Floor.objects.filter(section=self)

        # Итерация по этажам и суммирование small_square квартир
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor)
            total_shortened_square += sum(apartment.shortened_square * count_floor for apartment in apartments)

        return round(total_shortened_square, 2)

    def sum_s_shortened_square_section(self):
        total_shortened_square = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='s')
            total_shortened_square += sum(
                apartment.shortened_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_shortened_square, 2)

    def sum_k_shortened_square_section(self):
        total_shortened_square = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='1kk')
            total_shortened_square += sum(
                apartment.shortened_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_shortened_square, 2)

    def sum_kk_shortened_square_section(self):
        total_shortened_square = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='2kk')
            total_shortened_square += sum(
                apartment.shortened_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_shortened_square, 2)

    def sum_kkk_shortened_square_section(self):
        total_shortened_square = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='3kk')
            total_shortened_square += sum(
                apartment.shortened_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_shortened_square, 2)

    def sum_kkkk_shortened_square_section(self):
        total_shortened_square = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='4kk')
            total_shortened_square += sum(
                apartment.shortened_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_shortened_square, 2)

    def sum_kkkkk_shortened_square_section(self):
        total_shortened_square = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='5kk')
            total_shortened_square += sum(
                apartment.shortened_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_shortened_square, 2)

    def sum_kkkkkk_shortened_square_section(self):
        total_shortened_square = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='6kk')
            total_shortened_square += sum(
                apartment.shortened_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_shortened_square, 2)

    def sum_kkkkkkk_shortened_square_section(self):
        total_shortened_square = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='7kk')
            total_shortened_square += sum(
                apartment.shortened_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_shortened_square, 2)
    def sum_full_square_section(self):
        # Инициализируем сумму
        total_full_square = 0

        # Получаем все этажи, относящиеся к секции
        floors = Floor.objects.filter(section=self)

        # Итерация по этажам и суммирование small_square квартир
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor)
            total_full_square += sum(apartment.full_square * count_floor for apartment in apartments)

        return round(total_full_square, 2)

    def sum_s_full_square_section(self):
        total_full_square = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='s')
            total_full_square += sum(
                apartment.full_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_full_square, 2)

    def sum_k_full_square_section(self):
        total_full_square = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='1kk')
            total_full_square += sum(
                apartment.full_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_full_square, 2)

    def sum_kk_full_square_section(self):
        total_full_square = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='2kk')
            total_full_square += sum(
                apartment.full_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_full_square, 2)

    def sum_kkk_full_square_section(self):
        total_full_square = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='3kk')
            total_full_square += sum(
                apartment.full_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_full_square, 2)

    def sum_kkkk_full_square_section(self):
        total_full_square = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='4kk')
            total_full_square += sum(
                apartment.full_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_full_square, 2)

    def sum_kkkkk_full_square_section(self):
        total_full_square = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='5kk')
            total_full_square += sum(
                apartment.full_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_full_square, 2)

    def sum_kkkkkk_full_square_section(self):
        total_full_square = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='6kk')
            total_full_square += sum(
                apartment.full_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_full_square, 2)

    def sum_kkkkkkk_full_square_section(self):
        total_full_square = 0
        floors = Floor.objects.filter(section=self)
        for floor in floors:
            count_floor = floor.count_floor
            apartments = Apartment.objects.filter(floor=floor, type='7kk')
            total_full_square += sum(
                apartment.full_square * count_floor for apartment in apartments)  # Учитываем площадь квартир
        return round(total_full_square, 2)


    class Meta:
        verbose_name = 'Секция'
        verbose_name_plural = 'Секции'


class Floor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Этаж')
    count_floor = models.IntegerField(default=1, verbose_name='Количество этажей')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name='Секция')
    is_visible = models.BooleanField(default=True, verbose_name='Видимость')

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                                verbose_name='автор')

    def __str__(self):
        return self.name

    def sum_small_square_floor(self):
        return round(self.apartment_set.aggregate(models.Sum('small_square'))['small_square__sum'] or 0, 2)

    def sum_shortened_square_floor(self):
        return round(self.apartment_set.aggregate(models.Sum('shortened_square'))['shortened_square__sum'] or 0, 2)

    def sum_full_square_floor(self):
        return round(self.apartment_set.aggregate(models.Sum('full_square'))['full_square__sum'] or 0, 2)

    class Meta:
        verbose_name = 'Этаж'
        verbose_name_plural = 'Этажи'


class Apartment(models.Model):
    TYPES = [
        ("s", "Студии"),
        ("1kk", "1-комнатные"),
        ("2kk", "2-комнатные"),
        ("3kk", "3-комнатные"),
        ("4kk", "4-комнатные"),
        ("5kk", "5-комнатные"),
        ("6kk", "6-комнатные"),
        ("7kk", "7-комнатные")
    ]

    type = models.TextField(max_length=10, choices=TYPES, default="1kk", verbose_name='Тип квартиры')
    number = models.IntegerField(default=1, verbose_name='Номер квартиры в секции')
    small_square = models.FloatField(default=1, verbose_name='Площадь жилая')
    shortened_square = models.FloatField(default=1, verbose_name='Площадь с понижающими коэф.', **NULLABLE)
    full_square = models.FloatField(default=1, verbose_name='Площадь с летними', **NULLABLE)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, verbose_name='Этаж')
    is_visible = models.BooleanField(default=True, verbose_name='Видимость')

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                                verbose_name='автор')

    def __str__(self):
        return f"{self.type} - {self.small_square}"

    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'


@receiver(pre_save, sender=Section)
def set_section_name(sender, instance, **kwargs):
    if instance.name:
        instance.name = f"{instance.project.name}_{instance.name}"

@receiver(pre_save, sender=Floor)
def set_floor_name(sender, instance, **kwargs):
    if instance.name:
        instance.name = f"{instance.section.name}_{instance.name}"
