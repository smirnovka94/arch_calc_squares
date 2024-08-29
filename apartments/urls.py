from django.urls import path
from django.views.decorators.cache import cache_page

from apartments.apps import ApartmentsConfig
from apartments.views import (index, SectionCreateView, SectionListView, SectionDetailView, SectionUpdateView,
                              SectionDeleteView, ApartmentCreateView)

app_name = ApartmentsConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('section/create', SectionCreateView.as_view(), name='s_create'),
    path('section/list/', SectionListView.as_view(), name='list'),
    path('section/view/<int:pk>/', SectionDetailView.as_view(), name='view'),
    path('section/edit/<int:pk>/', SectionUpdateView.as_view(), name='edit'),
    path('section/delete/<int:pk>/', SectionDeleteView.as_view(), name='delete'),

    path('apartment/create', ApartmentCreateView.as_view(), name='a_create'),
    # path('section/list/', SectionListView.as_view(), name='list'),
    # path('section/view/<int:pk>/', SectionDetailView.as_view(), name='view'),
    # path('section/edit/<int:pk>/', SectionUpdateView.as_view(), name='edit'),
    # path('section/delete/<int:pk>/', SectionDeleteView.as_view(), name='delete'),
]

