from django.urls import path
from django.views.decorators.cache import cache_page
from django.urls import path
from apartments.views import (SectionDuplicateView, ToggleVisibilityView, ProjectDuplicateView, FloorDuplicateView,
                              export_excel, import_excel, your_import_view)


from apartments.apps import ApartmentsConfig
from apartments.views import (index, 
                              ProjectCreateView, ProjectListView, ProjectDetailView, ProjectUpdateView,
                              ProjectDeleteView,
                              SectionCreateView, SectionListView, SectionDetailView, SectionUpdateView,
                              SectionDeleteView,
                              ApartmentCreateView, ApartmentUpdateView, ApartmentDeleteView,
                              FloorCreateView, FloorUpdateView, FloorDeleteView
                              )
                              
app_name = ApartmentsConfig.name




urlpatterns = [
    path('', index, name='index'),
    path('project/<int:pk>/duplicate/', ProjectDuplicateView.as_view(), name='project_duplicate'),
    path('section/<int:pk>/duplicate/', SectionDuplicateView.as_view(), name='section_duplicate'),
    path('floor/<int:pk>/duplicate/', FloorDuplicateView.as_view(), name='floor_duplicate'),
    path('toggle-visibility/<int:pk>/<str:model>/', ToggleVisibilityView.as_view(), name='toggle_visibility'),

    path('project/create', ProjectCreateView.as_view(), name='p_create'),
    path('project/list/', ProjectListView.as_view(), name='p_list'),
    path('project/view/<int:pk>/', ProjectDetailView.as_view(), name='p_view'),
    path('project/edit/<int:pk>/', ProjectUpdateView.as_view(), name='p_edit'),
    path('project/delete/<int:pk>/', ProjectDeleteView.as_view(), name='p_delete'),
    
    path('section/create', SectionCreateView.as_view(), name='s_create'),
    path('section/list/', SectionListView.as_view(), name='s_list'),
    path('section/view/<int:pk>/', SectionDetailView.as_view(), name='s_view'),
    path('section/edit/<int:pk>/', SectionUpdateView.as_view(), name='s_edit'),
    path('section/delete/<int:pk>/', SectionDeleteView.as_view(), name='s_delete'),

    path('floor/create', FloorCreateView.as_view(), name='f_create'),
    path('floor/edit/<int:pk>/', FloorUpdateView.as_view(), name='f_edit'),
    path('floor/delete/<int:pk>/', FloorDeleteView.as_view(), name='f_delete'),

    path('apartment/create', ApartmentCreateView.as_view(), name='a_create'),
    path('apartment/edit/<int:pk>/', ApartmentUpdateView.as_view(), name='a_edit'),
    path('apartment/delete/<int:pk>/', ApartmentDeleteView.as_view(), name='a_delete'),

    path('export/', export_excel, name='export_excel'),
    path('import/', import_excel, name='import_excel'),
    # path('import2/', your_import_view, name='your_import_view'),

]

