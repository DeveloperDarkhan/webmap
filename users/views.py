from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.utils.translation import gettext_lazy as _

# Create your views here.


class ViewSignUp (CreateView):
    template_name = 'signup.html'
    form_class =CustomUserCreationForm
    success_url = reverse_lazy('signup_done')


class ViewSignUpAfter(TemplateView):
    template_name = 'singupafter.html'
    title = _('Created user')
    
# class ViewRessetpassword(CreateView):
#     template_name = 'registration/password_reset_form.html'
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('home')