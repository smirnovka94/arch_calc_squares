
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.forms import inlineformset_factory
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.shortcuts import render, redirect
from apartments.forms import SectionForm

from apartments.models import Section, Apartment


def index(request):
    sections = Section.objects.all()

    apartments = Apartment.objects.all()
    s_count, k_count, kk_count, kkk_count = 0, 0, 0, 0
    s_small_square, k_small_square, kk_small_square, kkk_small_square = 0, 0, 0, 0
    s_shortened_square, k_shortened_square, kk_shortened_square, kkk_shortened_square = 0, 0, 0, 0
    s_full_square, k_full_square, kk_full_square, kkk_full_square = 0, 0, 0, 0

    for apartment in apartments:
        section_number = apartment.section.number
        s_name = apartment.section.name

        a_type = apartment.type

        if a_type == "s":
            s_count += section_number
            s_small_square += apartment.small_square * section_number
            s_shortened_square += apartment.shortened_square * section_number
            s_full_square += apartment.full_square * section_number
        elif a_type == "1kk":
            k_count += section_number
            k_small_square += apartment.small_square * section_number
            k_shortened_square += apartment.shortened_square * section_number
            k_full_square += apartment.full_square * section_number
        elif a_type == "2kk":
            kk_count += section_number
            kk_small_square += apartment.small_square * section_number
            kk_shortened_square += apartment.shortened_square * section_number
            kk_full_square += apartment.full_square * section_number
        elif a_type == "3kk":
            kkk_count += section_number
            kkk_small_square += apartment.small_square * section_number
            kkk_shortened_square += apartment.shortened_square * section_number
            kkk_full_square += apartment.full_square * section_number
        else:
            pass

    sum_count = s_count + k_count + kk_count + kkk_count
    sum_small_square = s_small_square + k_small_square + kk_small_square + kkk_small_square
    sum_shortened_square = s_shortened_square + k_shortened_square + kk_shortened_square + kkk_shortened_square
    sum_full_square = s_full_square + k_full_square + kk_full_square + kkk_full_square


    a_s_count = Apartment.objects.filter(type="s").count()
    # a_s_small_square = Apartment.objects.filter(type="s").aggregate(total=Sum('small_square'))['total'] or 0
    # a_s_shortened_square = Apartment.objects.filter(type="s").aggregate(total=Sum('shortened_square'))['total'] or 0
    # a_s_full_square = Apartment.objects.filter(type="s").aggregate(total=Sum('full_square'))['total'] or 0

    a_1kk_count = Apartment.objects.filter(type="1kk").count(),
    # a_1kk_small_square = Apartment.objects.filter(type="1kk").aggregate(total=Sum('small_square'))['total'] or 0
    a_1kk_shortened_square = Apartment.objects.filter(type="1kk").aggregate(total=Sum('shortened_square'))['total'] or 0
    a_1kk_full_square = Apartment.objects.filter(type="1kk").aggregate(total=Sum('full_square'))['total'] or 0

    a_2kk_count = Apartment.objects.filter(type="2kk").count()
    # a_2kk_small_square = Apartment.objects.filter(type="2kk").aggregate(total=Sum('small_square'))['total'] or 0
    a_2kk_shortened_square = Apartment.objects.filter(type="2kk").aggregate(total=Sum('shortened_square'))['total'] or 0
    a_2kk_full_square = Apartment.objects.filter(type="2kk").aggregate(total=Sum('full_square'))['total'] or 0

    a_3kk_count = Apartment.objects.filter(type="3kk").count()
    # a_3kk_small_square = Apartment.objects.filter(type="3kk").aggregate(total=Sum('small_square'))['total'] or 0
    a_3kk_shortened_square = Apartment.objects.filter(type="3kk").aggregate(total=Sum('shortened_square'))['total'] or 0
    a_3kk_full_square = Apartment.objects.filter(type="3kk").aggregate(total=Sum('full_square'))['total'] or 0

    a_sum_count = Apartment.objects.count()
    # a_sum_small_square = Apartment.objects.aggregate(total=Sum('small_square'))['total'] or 0
    a_sum_shortened_square = Apartment.objects.aggregate(total=Sum('shortened_square'))[
                                'total'] or 0
    # sum_full_square = Apartment.objects.aggregate(total=Sum('full_square'))['total'] or 0

    context = {
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


class SectionCreateView(CreateView):
    model = Section
    fields = '__all__'
    success_url = reverse_lazy('apartments:index')

class SectionDetailView(DetailView):
    model = Section
    template_name = 'apartments/section_detail.html'
    context_object_name = 'sections'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['apartments'] = Apartment.objects.filter(section=self.object)
        return context


class SectionUpdateView(UpdateView):
    model = Section
    fields = '__all__'
    success_url = reverse_lazy('apartments:index')


class SectionDeleteView(DeleteView):
    model = Section
    success_url = reverse_lazy('apartments:index')


class SectionListView(ListView):
    model = Section
    template_name = 'apartments/section_list.html'
    context_object_name = 'sections'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.prefetch_related('apartment_set')  # 'apartment_set' – это обратная связь для ForeignKey
        return queryset

class ApartmentCreateView(CreateView):
    model = Apartment
    fields = '__all__'
    success_url = reverse_lazy('apartments:index')


class ApartmentUpdateView(UpdateView):
    model = Apartment
    fields = '__all__'
    success_url = reverse_lazy('apartments:index')


class ApartmentDeleteView(DeleteView):
    model = Apartment
    success_url = reverse_lazy('apartments:index')