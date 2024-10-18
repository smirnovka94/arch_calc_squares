from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from users.models import User


class UserForm (UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class VerificationForm(forms.Form):
    key = forms.CharField()


class ChangeForm_User(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()