from django.urls import path, include
from .views import *

urlpatterns = [
    path("", apiPage, name="api"),
]
