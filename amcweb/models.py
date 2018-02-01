from django.db import models

from mongoengine import *

# Create your models here.


class Patient(Document):
    """
    Represents a patient.
    """
    meta = {'collection': 'patients'}

    uid = IntField(min_value=1, unique=True, requied=True)
    first_name = StringField(max_length=150, required=True)
    last_name = StringField(max_length=150)
    gender = StringField(choices=['male', 'female', 'rather not mention'])
    dob = DateTimeField()
    contact = ListField(StringField(min_length=10, max_length=17), default=None, required=True)
    email = ListField(EmailField())
    address = DictField()  # { address, city, country }
    zip_code = IntField(min_value=1000)
    city = StringField(max_length=100)
    country = StringField(max_length=100)
    problem = StringField(max_length=200)
    doctor_feedback = StringField(max_length=200) # fraud patient etc
    comments = StringField(max_length=10000)
    # history of prescriptions from prescription collection
    # previous visits from appointment where turnedup = True


class Appointment(Document):
    """
    Represents an appointment.
    """
    meta = {'collection': 'appointments'}

    uid = IntField(min_value=1, unique=True, requied=True)
    datetime = DateTimeField(required=True)
    patient = DictField()
    new_patient = BooleanField(required=True)
    requested_on = DateTimeField(requied=True)
    purpose = StringField(max_length=500)
    requested_through = StringField(choices=['website', 'phone', 'email'])
    patient_turned_up = BooleanField()


class Prescription(Document):
    """
    Represents a prescription.
    """
    meta = {'collection': 'prescriptions'}

    uid = IntField(min_value=1, unique=True, requied=True)
    patient = DictField(requied=True)
    given_on = DateTimeField(required=True)
    appointment = DictField()
    problem = StringField(max_length=100)  # populate if no appointment
    feedback = StringField(choices=['positive', 'negative'])
    rating = IntField(choices=[1,2,3,4,5,6,7,8,9,10])
    rx = StringField(max_length=1000)  # actual prescription
    comments = StringField(max_length=10000)


class Counter(Document):
    """
    Maintains all the counters used in mongo.
    Used to perform auto-increment on fields.
    """
    name = StringField(max_length=10)
    count = IntField(min_value=1)
