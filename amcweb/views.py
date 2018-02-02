from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime, date

from amcweb.utils.mongo_utils import next_count
from .models import Appointment, Patient, Prescription


def index(request):
    html = ''

    return HttpResponse(f'This works {html}')
