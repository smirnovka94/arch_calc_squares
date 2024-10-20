from django import forms
from apartments.models import Section, Apartment, Floor


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
        
from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()