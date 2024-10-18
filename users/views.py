from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, FormView, UpdateView
from users.forms import UserForm, VerificationForm, ChangeForm_User
from users.models import User
import random
import string
import copy

random_key = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
_key = copy.copy(random_key)


class LoginView(BaseLoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('apartments:p_view')


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'


class UserVerificationView(FormView):
    form_class = VerificationForm
    success_url = reverse_lazy('apartments:home')
    template_name = 'apartments/home.html'

    def post(self, request, *args, **kwargs):
        key_post = request.POST.get('key_post')
        if _key == key_post:
            return redirect('users:login')
        else:
            return render(request, 'users/register.html', {'error_message': 'Ключи не совпадают'})

