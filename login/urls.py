from .views import *
from django.urls import re_path

urlpatterns = [
    re_path(r'^login/', login),
    re_path(r'^home/', home)
]
