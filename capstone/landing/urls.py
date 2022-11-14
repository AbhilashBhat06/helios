from django.urls import path, include
from .views import *

urlpatterns = [
    # path('', homePage.as_view()),
    # path('about', aboutPage.as_view()),
    # path('contact', contactPage.as_view()),
    # path('tech', techPage.as_view())
    path("", homePage, name="home"),
    path("about/", aboutPage, name="about"),
    path("contact/", contactPage, name="contact"),
    path("tech/", techPage, name="tech"),
    # path("api/", apiPage, name="api"),
]
