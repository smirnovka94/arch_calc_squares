from django.contrib import admin

from apartments.models import Apartment, Section

"""
@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
"""


class ApartmentInline(admin.TabularInline):
    model = Apartment
    extra = 1  # Количество пустых форм для добавления квартир по умолчанию


class SectionAdmin(admin.ModelAdmin):
    inlines = [ApartmentInline]  # Добавляем инлайн для квартир


admin.site.register(Section, SectionAdmin)
