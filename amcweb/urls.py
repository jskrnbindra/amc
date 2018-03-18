from django.urls import path

from . import views


app_name = 'amcweb'
urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('appointment', views.MakeAppointment.as_view(), name='appointment'),
    path('about', views.About.as_view(), name='about'),
    path('gallery', views.Gallery.as_view(), name='gallery'),
]
