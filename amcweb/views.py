from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from datetime import datetime, date

from amcweb.utils.mongo_utils import next_count
from .models import Appointment, Patient, Prescription


def index(request):
    patients = Patient.objects.all()
    context = {
        'patients': patients
    }

    return render(request, 'amcweb/index.html', context)


def reciever(request, pat_id):
    print(f'Received patient id: {pat_id}')

    return HttpResponse('Done')
