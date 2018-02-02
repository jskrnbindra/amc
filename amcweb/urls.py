from django.urls import path

from . import views


app_name = 'amcweb'
urlpatterns = [
    path('', views.index, name='index'),
    path('reciever/<int:pat_id>', views.reciever, name='reciever')
]
