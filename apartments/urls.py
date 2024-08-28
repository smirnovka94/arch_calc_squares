from django.urls import path
from django.views.decorators.cache import cache_page

from apartments.apps import ApartmentsConfig
from apartments.views import index, create_section #SectionCreatelView

app_name = ApartmentsConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('section/create', create_section, name='section_create'),
    # path('delete_section/', section_delete, name='delete_section'),
]

