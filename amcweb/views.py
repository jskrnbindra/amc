from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from amcweb.utils.mongo_utils import next_count
from . import models


def index(request):
    billu = models.Patient(next_count('Patient'), 'bhalus', contact=['9988355277']).save()
    appo = models.Appointment(next_count('Appointment'), datetime=date(2018, 1, 21), new_patient=False, requested_on=date(2017, 12, 22), patient=billu.__dict__)
    presc = models.Prescription(next_count('Prescription'), patient=billu.__dict__, given_on=date(2018, 1, 21), appointment=appo.__dict__, problem='godeyan ch dard', feedback='positive', rating=8, rx='roz nahao bai ji').save()

    return HttpResponse('This works')


# todo: How to store document in another document, try all field types and base class types for models. Else use class to dict conversion
