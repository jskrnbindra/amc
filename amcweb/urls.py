from django.urls import path

from . import views


app_name = 'amcweb'
urlpatterns = [
    path('', views.index, name='index'),
]
