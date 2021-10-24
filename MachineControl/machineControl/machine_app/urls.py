from django.conf.urls import url
from machine_app import views

urlpatterns = [
    # url(r'^$', views.index, name = 'index'),
    # url(r'^dashboard/', views.index, name = 'index'),
    url(r'^adduser/', views.addUser, name = 'addUser'),
    # url(r'^additem/', views.index, name = 'index'),
    # url(r'^editstuff/', views.index, name = 'index'),
    # url(r'^salsorder', views.index, name = 'index'),
    # url(r'^updateamount/', views.index, name = 'index'),
    # url(r'^productionplan', views.index, name = 'index'),
]