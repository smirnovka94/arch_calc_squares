import pandas as pd
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.shortcuts import render, redirect
from apartments.models import Project, Section, Apartment, Floor
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    sections = Section.objects.all()
    floors = Floor.objects.all()
    apartments = Apartment.objects.all()
    
    s_count, k_count, kk_count, kkk_count = 0, 0, 0, 0
    s_small_square, k_small_square, kk_small_square, kkk_small_square = 0, 0, 0, 0
    s_shortened_square, k_shortened_square, kk_shortened_square, kkk_shortened_square = 0, 0, 0, 0
    s_full_square, k_full_square, kk_full_square, kkk_full_square = 0, 0, 0, 0

    for apartment in apartments:
        floor_count = apartment.floor.count_floor
        
        a_type = apartment.type

        if a_type == "s":
            s_count += floor_count
            s_small_square += apartment.small_square * floor_count
            s_shortened_square += apartment.shortened_square * floor_count
            s_full_square += apartment.full_square * floor_count
        elif a_type == "1kk":
            k_count += floor_count
            k_small_square += apartment.small_square * floor_count
            k_shortened_square += apartment.shortened_square * floor_count
            k_full_square += apartment.full_square * floor_count
        elif a_type == "2kk":
            kk_count += floor_count
            kk_small_square += apartment.small_square * floor_count
            kk_shortened_square += apartment.shortened_square * floor_count
            kk_full_square += apartment.full_square * floor_count
        elif a_type == "3kk":
            kkk_count += floor_count
            kkk_small_square += apartment.small_square * floor_count
            kkk_shortened_square += apartment.shortened_square * floor_count
            kkk_full_square += apartment.full_square * floor_count
        else:
            pass

    sum_count = s_count + k_count + kk_count + kkk_count
    sum_small_square = s_small_square + k_small_square + kk_small_square + kkk_small_square
    sum_shortened_square = s_shortened_square + k_shortened_square + kk_shortened_square + kkk_shortened_square
    sum_full_square = s_full_square + k_full_square + kk_full_square + kkk_full_square


    # a_s_count = Apartment.objects.filter(type="s").count()
    #
    # a_1kk_count = Apartment.objects.filter(type="1kk").count()
    # # a_1kk_small_square = Apartment.objects.filter(type="1kk").aggregate(total=Sum('small_square'))['total'] or 0
    # a_1kk_shortened_square = Apartment.objects.filter(type="1kk").aggregate(total=Sum('shortened_square'))['total'] or 0
    # a_1kk_full_square = Apartment.objects.filter(type="1kk").aggregate(total=Sum('full_square'))['total'] or 0
    #
    # a_2kk_count = Apartment.objects.filter(type="2kk").count()
    # # a_2kk_small_square = Apartment.objects.filter(type="2kk").aggregate(total=Sum('small_square'))['total'] or 0
    # a_2kk_shortened_square = Apartment.objects.filter(type="2kk").aggregate(total=Sum('shortened_square'))['total'] or 0
    # a_2kk_full_square = Apartment.objects.filter(type="2kk").aggregate(total=Sum('full_square'))['total'] or 0
    #
    # a_3kk_count = Apartment.objects.filter(type="3kk").count()
    # # a_3kk_small_square = Apartment.objects.filter(type="3kk").aggregate(total=Sum('small_square'))['total'] or 0
    # a_3kk_shortened_square = Apartment.objects.filter(type="3kk").aggregate(total=Sum('shortened_square'))['total'] or 0
    # a_3kk_full_square = Apartment.objects.filter(type="3kk").aggregate(total=Sum('full_square'))['total'] or 0
    #
    # a_sum_count = Apartment.objects.count()
    # # a_sum_small_square = Apartment.objects.aggregate(total=Sum('small_square'))['total'] or 0
    # a_sum_shortened_square = Apartment.objects.aggregate(total=Sum('shortened_square'))[
    #                             'total'] or 0
    # # sum_full_square = Apartment.objects.aggregate(total=Sum('full_square'))['total'] or 0

    projects = Project.objects.all()

    context = {

        'projects': projects,
        'object_list': Section.objects.all().order_by('name'),

        's_count': s_count,
        's_small_square': round(s_small_square, 2),
        's_shortened_square': s_shortened_square,
        's_full_square': s_full_square,

        '1kk_count': k_count,
        '1kk_small_square': round(k_small_square, 2),
        '1kk_shortened_square': round(k_shortened_square, 2),
        '1kk_full_square': round(k_full_square, 2),

        '2kk_count': kk_count,
        '2kk_small_square': round(kk_small_square, 2),
        '2kk_shortened_square': round(kk_shortened_square, 2),
        '2kk_full_square': round(kk_full_square, 2),

        '3kk_count': kkk_count,
        '3kk_small_square': round(kkk_small_square, 2),
        '3kk_shortened_square': round(kkk_shortened_square, 2),
        '3kk_full_square': round(kkk_full_square, 2),


        'sum_count': sum_count,
        'sum_small_square': round(sum_small_square, 2),
        'sum_shortened_square': round(sum_shortened_square, 2),
        'sum_full_square': round(sum_full_square, 2),



    }
    return render(request, 'apartments/index.html', context)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['name']
    success_url = reverse_lazy('apartments:p_list')

    def form_valid(self, form):
        form.instance.creator = self.request.user  # Устанавливаем текущего пользователя как создателя
        return super().form_valid(form)


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'apartments/project_detail.html'
    context_object_name = 'project'

class ProjectUpdateView(UpdateView):
    model = Project
    fields = ['name']
    success_url = reverse_lazy('apartments:p_list')


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('apartments:p_list')


class ProjectListView(ListView):
    model = Project
    template_name = 'apartments/project_list.html'
    context_object_name = 'projects'


class ProjectDuplicateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        project = Project.objects.get(pk=pk)
        new_project_count = Project.objects.filter(name__startswith=f"{project.name}-копия").count() + 1
        new_project_name = f"{project.name}-копия {new_project_count}"

        # Создаем новый проект
        new_project = Project.objects.create(
            name=new_project_name,
            creator=request.user,
        )

        # Копируем секции
        for section in project.sections.all():
            new_section = Section.objects.create(
                name=section.name,
                project=new_project,
                creator=request.user,
                is_visible=section.is_visible,
            )

            # Копируем этажи
            for floor in section.floor_set.all():
                new_floor = Floor.objects.create(
                    name=floor.name,
                    count_floor=floor.count_floor,
                    section=new_section,
                    creator=request.user,
                    is_visible=floor.is_visible,
                )

                # Копируем квартиры
                for apartment in floor.apartment_set.all():
                    Apartment.objects.create(
                        type=apartment.type,
                        number=apartment.number,
                        small_square=apartment.small_square,
                        shortened_square=apartment.shortened_square,
                        full_square=apartment.full_square,
                        floor=new_floor,
                        creator=request.user,
                        is_visible=apartment.is_visible,
                    )

        return redirect('apartments:p_list')


class SectionCreateView(LoginRequiredMixin, CreateView):
    model = Section
    fields = ['name', 'project']

    def form_valid(self, form):
        form.instance.creator = self.request.user  # Устанавливаем текущего пользователя как создателя
        section = form.save()
        return HttpResponseRedirect(reverse('apartments:p_view', args=[section.project.pk]))
        return super().form_valid(form)



class SectionDetailView(DetailView):
    model = Section
    template_name = 'apartments/project_detail.html'
    context_object_name = 'sections'



class SectionUpdateView(UpdateView):
    model = Section
    fields = ['name']
    # success_url = reverse_lazy('apartments:index')

    def form_valid(self, form):
        section = form.save()
        # Перенаправляем на страницу проекта
        return HttpResponseRedirect(reverse('apartments:p_view', args=[section.project.pk]))


class SectionDeleteView(DeleteView):
    model = Section

    def get_success_url(self):
        # Перенаправление на страницу проекта после удаления секции
        return reverse('apartments:p_view', args=[self.object.project.pk])

class SectionListView(ListView):
    model = Section
    template_name = 'apartments/project_list.html'
    context_object_name = 'sections'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs).filter(creator=self.request.user)
        queryset = queryset.prefetch_related('floor_set')  # Предзагрузите этажи
        return queryset


class SectionDuplicateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        # Получаем объект секции по первичному ключу (pk)
        section = get_object_or_404(Section, pk=pk)

        # Создаем дубликат секции
        new_section = Section.objects.create(
            name=f"{section.name}-к1",
            project=section.project,
            creator=request.user,
            is_visible=section.is_visible
        )

        # Логика для копирования всех зависимостей (floor & apartments)
        for floor in section.floor_set.all():
            new_floor = Floor.objects.create(
                name=f"{floor.name}-к1",
                count_floor=floor.count_floor,
                section=new_section,
                creator=request.user,
                is_visible=floor.is_visible
            )
            for apartment in floor.apartment_set.all():
                Apartment.objects.create(
                    type=apartment.type,
                    number=apartment.number,
                    small_square=apartment.small_square,
                    shortened_square=apartment.shortened_square,
                    full_square=apartment.full_square,
                    floor=new_floor,
                    creator=request.user,
                    is_visible=apartment.is_visible
                )

        # Перенаправляем пользователя к представлению проекта
        return redirect('apartments:p_view', pk=section.project.pk)  # Используем pk секции для получения проекта

class ToggleVisibilityView(LoginRequiredMixin, View):
    def post(self, request, pk, model):
        if model == 'section':
            section = Section.objects.get(pk=pk)
            section.is_visible = not section.is_visible
            section.save()
        elif model == 'floor':
            floor = Floor.objects.get(pk=pk)
            floor.is_visible = not floor.is_visible
            floor.save()
        elif model == 'apartment':
            apartment = Apartment.objects.get(pk=pk)
            apartment.is_visible = not apartment.is_visible
            apartment.save()
        return redirect(request.META.get('HTTP_REFERER', 'apartments:index'))


class FloorCreateView(CreateView):
    model = Floor
    fields = ['name', 'count_floor', 'section', ]

    def form_valid(self, form):
        form.instance.creator = self.request.user  # Устанавливаем текущего пользователя как создателя
        floor = form.save()
        return HttpResponseRedirect(reverse('apartments:p_view', args=[floor.section.project.pk]))
        return super().form_valid(form)


class FloorDuplicateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        # Получаем объект секции по первичному ключу (pk)
        floor = get_object_or_404(Floor, pk=pk)

        # Создаем дубликат секции
        new_floor = Floor.objects.create(
            name=f"{floor.name}-к1",
            section=floor.section,
            creator=request.user,
            is_visible=floor.is_visible
        )


        for apartment in floor.apartment_set.all():
            Apartment.objects.create(
                type=apartment.type,
                number=apartment.number,
                small_square=apartment.small_square,
                shortened_square=apartment.shortened_square,
                full_square=apartment.full_square,
                floor=new_floor,
                creator=request.user,
                is_visible=apartment.is_visible
            )

        # Перенаправляем пользователя к представлению проекта
        return redirect('apartments:p_view', pk=floor.section.project.pk)  # Используем pk секции для получения проекта



class FloorUpdateView(UpdateView):
    model = Floor
    fields = ['name', 'count_floor', 'section', ]

    def form_valid(self, form):
        floor = form.save()
        # Перенаправляем на страницу проекта
        return HttpResponseRedirect(reverse('apartments:p_view', args=[floor.section.project.pk]))

class FloorDetailView(DetailView):
    model = Floor
    template_name = 'apartments/floor_detail.html'  # Название вашего шаблона

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем все квартиры для текущего этажа и сортируем их по номеру
        context['apartments'] = self.object.apartment_set.all().order_by('number')
        return context

class FloorDeleteView(DeleteView):
    model = Floor
    success_url = reverse_lazy('apartments:index')

    def get_success_url(self):
        # Перенаправление на страницу проекта после удаления этажа
        return reverse('apartments:p_view', args=[self.object.section.project.pk])


class ApartmentCreateView(CreateView):
    model = Apartment
    fields = ['type', 'number', 'small_square', 'shortened_square', 'full_square', 'floor', ]

    def form_valid(self, form):
        form.instance.creator = self.request.user  # Устанавливаем текущего пользователя как создателя
        apartment = form.save()
        return HttpResponseRedirect(reverse('apartments:p_view', args=[apartment.floor.section.project.pk]))
        return super().form_valid(form)


class ApartmentUpdateView(UpdateView):
    model = Apartment
    fields = ['type', 'number', 'small_square', 'shortened_square', 'full_square', 'floor', ]

    def form_valid(self, form):
        apartment = form.save()
        # Перенаправляем на страницу проекта
        return HttpResponseRedirect(reverse('apartments:p_view', args=[apartment.floor.section.project.pk]))


class ApartmentDeleteView(DeleteView):
    model = Apartment

    def get_success_url(self):
        # Перенаправление на страницу проекта после удаления квартиры
        return reverse('apartments:p_view', args=[self.object.floor.section.project.pk])

def export_excel(request):
    projects = Project.objects.all()
    data = []

    for project in projects:
        for section in project.sections.all():
            for floor in section.floor_set.all():
                for apartment in floor.apartment_set.all():
                    data.append({
                        'Project Name': project.name,
                        'Section Name': section.name,
                        'Floor Name': floor.name,
                        'Apartment Type': apartment.type,
                        'Apartment Number': apartment.number,
                        'Small Square': apartment.small_square,
                        'Shortened Square': apartment.shortened_square,
                        'Full Square': apartment.full_square,
                    })

    df = pd.DataFrame(data)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=projects.xlsx'

    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)

    return response

"""def import_excel(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        df = pd.read_excel(file)

        for _, row in df.iterrows():
            project, created = Project.objects.get_or_create(name=row['Project Name'])
            section, _ = Section.objects.get_or_create(name=row['Section Name'], project=project)
            floor, _ = Floor.objects.get_or_create(name=row['Floor Name'], section=section)
            Apartment.objects.get_or_create(
                type=row['Apartment Type'],
                number=row['Apartment Number'],
                small_square=row['Small Square'],
                shortened_square=row['Shortened Square'],
                full_square=row['Full Square'],
                floor=floor
            )

        return render(request, 'import_result.html', {'message': 'Import successful!'})

    return render(request, 'import_excel.html')
"""


def import_excel(request):


    if request.method == 'POST' and request.FILES['excel_file']:  # Изменено с 'file' на 'excel_file'
        file = request.FILES['excel_file']  # Изменено с 'file' на 'excel_file'
        df = pd.read_excel(file)
        for _, row in df.iterrows():
            # Получаем или создаем проект
            project, created = Project.objects.get_or_create(name=row['Project Name'])
            # Получаем или создаем секцию
            section, created = Section.objects.get_or_create(name=row['Section Name'], project=project)
            # Получаем или создаем этаж
            floor, created = Floor.objects.get_or_create(name=row['Floor Name'], section=section)
            # Получаем или создаем квартиру
            Apartment.objects.get_or_create(
                type=row['Apartment Type'],
                number=row['Apartment Number'],
                small_square=row['Small Square'],
                shortened_square=row['Shortened Square'],
                full_square=row['Full Square'],
                floor=floor
            )
        return HttpResponse("Данные успешно импортированы.")
    return render(request, 'import_excel.html')


def your_import_view(request):
    if request.method == 'POST' and request.FILES['excel_file']:  # Изменено с 'file' на 'excel_file'
        file = request.FILES['excel_file']  # Изменено с 'file' на 'excel_file'
        df = pd.read_excel(file)
        for _, row in df.iterrows():
            # Получаем или создаем проект
            project, created = Project.objects.get_or_create(name=row['Project Name'])
            # Получаем или создаем секцию
            section, created = Section.objects.get_or_create(name=row['Section Name'], project=project)
            # Получаем или создаем этаж
            floor, created = Floor.objects.get_or_create(name=row['Floor Name'], section=section)
            # Получаем или создаем квартиру
            Apartment.objects.get_or_create(
                type=row['Apartment Type'],
                number=row['Apartment Number'],
                small_square=row['Small Square'],
                shortened_square=row['Shortened Square'],
                full_square=row['Full Square'],
                floor=floor
            )
        return HttpResponse("Данные успешно импортированы.")
    return render(request, 'import_excel.html')

