from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.aposta, name='aposta'),
    url(r'^(?P<aposta_id>[0-9]+)/$', views.detalhe, name='detalhe'),
    url(r'^novaaposta/$', views.novaaposta, name='novaaposta'),
    url(r'^gravaAposta/$', views.gravaAposta, name='gravaAposta'),
]