from django.contrib import admin

from apartments.models import Apartment, Section


class ApartmentInline(admin.TabularInline):
    model = Apartment
    extra = 1  # Количество пустых форм для добавления квартир по умолчанию


class SectionAdmin(admin.ModelAdmin):
    inlines = [ApartmentInline]  # Добавляем инлайн для квартир


admin.site.register(Section, SectionAdmin)
