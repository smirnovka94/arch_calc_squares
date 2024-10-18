from django import forms
# from django.forms import inlineformset_factory
from apartments.models import Section, Apartment, Floor

"""

class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['type']  # Укажите необходимые поля

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['name', 'number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apartment_forms = [ApartmentForm(prefix=f'apartment_{i}') for i in range(1)]

    def save(self, commit=True):
        section = super().save(commit=commit)
        if commit:
            section.save()
            for form in self.apartment_forms:
                apartment = form.save(commit=False)
                apartment.section = section  # Устанавливаем связь с Section
                apartment.save()
        return section

"""

class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        exclude = ('creator', )


class FloorForm(forms.ModelForm):
    class Meta:
        model = Floor
        exclude = ('creator', )


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        exclude = ('creator', )
        
