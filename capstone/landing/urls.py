from django.urls import path, include
from .views import *

urlpatterns = [
	# path('', homePage.as_view()),
	# path('about', aboutPage.as_view()),
	# path('contact', contactPage.as_view()),
	# path('tech', techPage.as_view())
	path('', homePage),
	path('about/', aboutPage),
	path('contact/', contactPage),
	path('tech/', techPage)
]
