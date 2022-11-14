from rest_framework.routers import DefaultRouter
from django.urls import path, include
from landing.views import homePage, aboutPage, contactPage, techPage
from landing.views import buildingsViewSet
from landing.views import MLAlgorithmViewSet
from landing.views import MLAlgorithmStatusViewSet
from landing.views import MLRequestViewSet

# from .views import apiPage

router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", buildingsViewSet, basename="buildings")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(
    r"mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses"
)
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")

urlpatterns = [
    # path("", apiPage, name="api"),
    path("api/v1/", include(router.urls)),
]
