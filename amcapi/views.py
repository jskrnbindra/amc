from django.http import HttpResponse, HttpResponseServerError, HttpResponseNotFound

from amcweb.models import Patient


def patient(request, patient_id):
    try:
        queryset = Patient.objects(uid=patient_id)
        if len(queryset) == 0:
            response = HttpResponseNotFound()
        else:
            response = HttpResponse({'name': queryset[0]['first_name']}.__repr__().replace("'", '"'))
    except:
        response = HttpResponseServerError()

    return response
