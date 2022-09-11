from django.urls import path, include
from .views import homePage

urlpatterns = [
	path('', homePage.as_view()),
]
