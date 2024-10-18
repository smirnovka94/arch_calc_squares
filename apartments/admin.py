from django.contrib import admin

from apartments.models import Apartment, Floor, Section

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    list_display = ('section', 'name', 'count_floor', )

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('floor', 'type', 'number', 'small_square', 'shortened_square', 'full_square', )

"""
class ApartmentInline(admin.TabularInline):
    model = Apartment
    extra = 1  # Количество пустых форм для добавления квартир по умолчанию


class SectionAdmin(admin.ModelAdmin):
    inlines = [ApartmentInline]  # Добавляем инлайн для квартир


admin.site.register(Section, SectionAdmin)

"""
