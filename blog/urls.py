from django.conf.urls import include, url
from .import views

urlpatterns = [
    url(r'^$', views.primer_vista, name= 'primer_vista'),
]
