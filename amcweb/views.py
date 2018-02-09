from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .forms import AppointmentForm
from .models import Appointment, Patient, Prescription


class About(TemplateView):
    template_name = 'amcweb/about.html'


class Index(TemplateView):
    template_name = 'amcweb/index.html'


class MakeAppointment(FormView):
    template_name = 'amcweb/appointment.html'
    form_class = AppointmentForm

    def form_valid(self, form):
        form.create_appointment(form.cleaned_data)
        return render(self.request, 'amcweb/appointment.html', {'msg': {'msg': 'ye le', 'only': True, 'appointment': form.cleaned_data}})

    def form_invalid(self, form):
        print('Form invalid')
        print(form.errors)
        return super().form_invalid(form)
