from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .forms import AppointmentForm, SubscribeEmail
from .handlers.subscribe_form import new_subscriber_handler
from .models import Appointment, Patient, Prescription  # Do not remove these dependencies, they're used
from .utils.mailer import mail


def index(request):
    if request.method == 'POST':
        context = new_subscriber_handler(request)
        return render(request, 'amcweb/index.html', context)

    return render(request, 'amcweb/index.html', {})


class About(TemplateView):
    template_name = 'amcweb/about.html'


class MakeAppointment(FormView):
    template_name = 'amcweb/appointment.html'
    form_class = AppointmentForm

    def form_valid(self, form):
        form.create_appointment(form.cleaned_data)
        mail('new_appointment', {'name': form.cleaned_data['name'], 'email': form.cleaned_data['email']})
        return render(self.request, 'amcweb/appointment.html', {'msg': {'msg': 'ye le', 'only': True, 'appointment': form.cleaned_data}})

    def form_invalid(self, form):
        print('Form invalid')
        print(form.errors)
        return super().form_invalid(form)
