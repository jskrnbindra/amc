from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from datetime import datetime, date

from amcweb.utils.mongo_utils import next_count
from .models import Appointment, Patient, Prescription


def index(request):
    return render(request, 'amcweb/index.html', {})

