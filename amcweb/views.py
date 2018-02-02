from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from amcweb.utils.mongo_utils import next_count
from . import models


def index(request):

    # presc = models.Prescription(next_count('Prescription'), given_on=date(2018, 1, 21))
    # appo = models.Appointment(next_count('Appointment'), datetime=date(2018, 1, 11), new_patient=False, requested_on=date(2018, 1, 21))
    # apps = []
    # prescs = []
    # apps.append(appo)
    # prescs.append(presc)
    # pat = models.Patient(next_count('Patients'), first_name="billa badmash", contact=['998899889988'], prescriptions=prescs, appointments=apps)
    #
    print(models.Patient.objects.get(uid=9).prescriptions.get(uid=15).given_on)

    return HttpResponse('This works')


# todo: How to store document in another document, try all field types and base class types for models. Else use class to dict conversion
