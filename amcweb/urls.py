from django.urls import path

from . import views


app_name = 'amcweb'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('index', views.Index.as_view(), name='index'),
    path('appointment', views.MakeAppointment.as_view(), name='appointment'),
    path('about', views.About.as_view(), name='about'),
]
