from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r"^$", views.startside, name='startside'),
    url(r"^lanser$", views.lanser, name='lanser'),
    url(r"^valgtlanse$", views.valgtlanse, name='valgtlanse'),
  ]