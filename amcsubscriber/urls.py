from django.urls import path, include
from django.views.generic import RedirectView

from . import views

app_name = 'amcsubscriber'
urlpatterns = [
    path('email', views.SubEmail.as_view(), name='subscribe_email'),
    path('', RedirectView.as_view(url='/')),
    path(r'^$', RedirectView.as_view(url='/'))
]
