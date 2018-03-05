from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r"^$", views.home, name='home'),
    url(r'^submit', views.submit)
  ]