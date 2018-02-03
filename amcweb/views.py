from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .forms import AppointmentForm
from .models import Appointment, Patient, Prescription


class Index(TemplateView):
    template_name = 'amcweb/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Appointment(FormView):
    template_name = 'amcweb/appointment.html'
    form_class = AppointmentForm
    success_url = '/appointment'

    def form_valid(self, form):

        print(form.cleaned_data)
        form.send_email()
        return super().form_valid(form)


class About(TemplateView):
    template_name = 'amcweb/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
