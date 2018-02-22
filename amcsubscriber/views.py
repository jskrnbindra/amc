from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .forms import SubscribeEmail
# from .models import Appointment, Patient, Prescription


class SubEmail(FormView):
    template_name = 'amcweb/master.html'
    form_class = SubscribeEmail
    current_app = 'amcweb'

    def form_valid(self, form):
        print('valid form')
        return render(self.request, 'amcweb/appointment.html', {'msg': {'msg': 'ye le', 'only': True, 'appointment': form.cleaned_data}})

