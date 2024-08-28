from django import forms
from django.forms import inlineformset_factory
from apartments.models import Section, Apartment


class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['type', 'number', 'small_square', 'shortened_square', 'full_square']


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['name', 'number']

ApartmentFormSet = inlineformset_factory(Section, Apartment, form=ApartmentForm, extra=1)

