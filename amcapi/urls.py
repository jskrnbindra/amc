from django.urls import path

from . import views

app_name = 'amcapi'
urlpatterns = [
    path('patient/<int:patient_id>/', views.patient, name='patient'),
]
