
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from apartments.forms import SectionForm, ApartmentFormSet

from apartments.models import Section, Apartment


def index(request):
    context = {
        'object_list': Section.objects.all(),
        'count': '32 кв',
        'count_s': '6 студий',
        'count_1': '12 1кк',
        'count_2': '4 4кк',
        'count_3': '10 3кк',

    }
    return render(request, 'apartments/index.html', context)

"""
class SectionCreatelView(CreateView):
    model = Section
    fields = SectionForm
    template_name = 'apartments/section_form.html'
    success_url = reverse_lazy('apartments:index')

    def form_valid(self, form):
        # Сначала сохраняем объект Section
        section = form.save()

        apartments = form.cleaned_data.get('apartments')
        if apartments:
            for apartment in apartments:
                apartment.Section = section
                apartment.save()

        return super().form_valid(form)
"""
def create_section(request):
    if request.method == 'POST':
        section_form = SectionForm(request.POST)
        formset = ApartmentFormSet(request.POST, instance=section_form.instance)

        if section_form.is_valid() and formset.is_valid():
            section = section_form.save()
            apartments = formset.save(commit=False)
            for apartment in apartments:
                apartment.section = section
                apartment.save()

            return redirect('apartments:index')

    else:
        section_form = SectionForm()
        formset = ApartmentFormSet()

    return render(request, 'apartments/section_form.html', {'section_form': section_form, 'formset': formset})

"""
class SectionUpdatelView(UpdateView):
    model = Section
    form_class = SectionForm

class SectionDeleteView(DeleteView):
    model = Section
    success_url = reverse_lazy('main:home')




from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Section

def index(request):
    context = {
        'object_list': Section.objects.all(),
    }
    return render(request, 'apartments/!home.html', context)

def section_update(request):
    if request.method == "POST":
        section_id = request.POST.get('id')
        name = request.POST.get('name')
        number = request.POST.get('number')

        section, created = Section.objects.update_or_create(
            id=section_id,
            defaults={'name': name, 'number': number}
        )
        return JsonResponse({'id': section.id, 'name': section.name, 'number': section.number})

def section_delete(request):
    if request.method == "POST":
        section_id = request.POST.get('id')
        Section.objects.filter(id=section_id).delete()
        return JsonResponse({'success': True})
"""