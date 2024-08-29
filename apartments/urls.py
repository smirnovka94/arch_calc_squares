from django.urls import path
from django.views.decorators.cache import cache_page

from apartments.apps import ApartmentsConfig
from apartments.views import (index, SectionCreateView, SectionListView, SectionDetailView, SectionUpdateView,
                              SectionDeleteView,
                              ApartmentCreateView, ApartmentUpdateView, ApartmentDeleteView)

app_name = ApartmentsConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('section/create', SectionCreateView.as_view(), name='s_create'),
    path('section/list/', SectionListView.as_view(), name='s_list'),
    path('section/view/<int:pk>/', SectionDetailView.as_view(), name='s_view'),
    path('section/edit/<int:pk>/', SectionUpdateView.as_view(), name='s_edit'),
    path('section/delete/<int:pk>/', SectionDeleteView.as_view(), name='s_delete'),

    path('apartment/create', ApartmentCreateView.as_view(), name='a_create'),
    # path('apartment/list/', SectionListView.as_view(), name='list'),
    # path('apartment/view/<int:pk>/', SectionDetailView.as_view(), name='view'),
    path('apartment/edit/<int:pk>/', ApartmentUpdateView.as_view(), name='a_edit'),
    path('apartment/delete/<int:pk>/', ApartmentDeleteView.as_view(), name='a_delete'),
]

