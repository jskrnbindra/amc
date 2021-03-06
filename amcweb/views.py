from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .forms import AppointmentForm
from .handlers.subscribe_form import new_subscriber_handler, new_whatsapp_subscriber_handler
from amcweb.utils.notifications.mailer import mail
from amcweb.utils.notifications.smser import send_sms


def index(request):
    if request.method == 'POST':
        if request.POST['type'] == 'subscribe':
            context = new_subscriber_handler(request)
            return render(request, 'amcweb/index.html', context)
        elif request.POST['type'] == 'whatsapp_subscribe':
            context = new_whatsapp_subscriber_handler(request)
            return render(request, 'amcweb/index.html', context)

    return render(request, 'amcweb/index.html', {})


class About(TemplateView):
    template_name = 'amcweb/about.html'


class Gallery(TemplateView):
    template_name = 'amcweb/gallery.html'


class MakeAppointment(FormView):
    template_name = 'amcweb/appointment.html'
    form_class = AppointmentForm

    def form_valid(self, form):
        form.create_appointment(form.cleaned_data)
        mail('new_appointment', {'name': form.cleaned_data['name'], 'email': form.cleaned_data['email']})
        send_sms('new_appointment', {'name': form.cleaned_data['name'], 'numbers': form.cleaned_data['contact']})
        return render(self.request, 'amcweb/appointment.html', {'msg': {'msg': 'ye le', 'only': True, 'appointment': form.cleaned_data}})

    def form_invalid(self, form):
        print('Form invalid')
        print(form.errors)
        return super().form_invalid(form)


class Treatments(TemplateView):
    template_name = 'amcweb/treatments.html'
