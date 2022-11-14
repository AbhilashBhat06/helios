from django.urls import path, include
from .views import homePage, aboutPage, contactPage, techPage

"""
from landing.views import buildingsViewSet
from landing.views import MLAlgorithmViewSet
from landing.views import MLAlgorithmStatusViewSet
from landing.views import MLRequestViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", buildingsViewSet, basename="buildings")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(
    r"mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses"
)
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")

urlpatterns += [
    path("api/v1/", include(router.urls)),
]
"""
urlpatterns = [
    # path('', homePage.as_view()),
    # path('about', aboutPage.as_view()),
    # path('contact', contactPage.as_view()),
    # path('tech', techPage.as_view())
    path("", homePage, name="home"),
    path("about/", aboutPage, name="about"),
    path("contact/", contactPage, name="contact"),
    path("tech/", techPage, name="tech"),
]
