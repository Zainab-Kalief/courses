from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.addCourse),
    url(r'^destroy/(?P<id>\d+)$', views.removeButton),
    url(r'^delete/(?P<id>\d+)$', views.destroy),

]
