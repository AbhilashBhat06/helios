from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework import mixins
from landing.models import buildings
from landing.serializers import buildingsSerializer
from landing.models import MLAlgorithm
from landing.serializers import MLAlgorithmSerializer
from landing.models import MLAlgorithmStatus
from landing.serializers import MLAlgorithmStatusSerializer
from landing.models import MLRequest
from landing.serializers import MLRequestSerializer


# def apiPage(req):
#     return render(req, "api.html")


class buildingsViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = buildingsSerializer
    queryset = buildings.objects.all()


class MLAlgorithmViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = MLAlgorithmSerializer
    queryset = MLAlgorithm.objects.all()


def deactivate_other_statuses(instance):
    old_statuses = MLAlgorithmStatus.objects.filter(
        parent_mlalgorithm=instance.parent_mlalgorithm,
        created_at__lt=instance.created_at,
        active=True,
    )
    for i in range(len(old_statuses)):
        old_statuses[i].active = False
    MLAlgorithmStatus.objects.bulk_update(old_statuses, ["active"])


class MLAlgorithmStatusViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
):
    serializer_class = MLAlgorithmStatusSerializer
    queryset = MLAlgorithmStatus.objects.all()

    def perform_create(self, serializer):
        try:
            with transaction.atomic():
                instance = serializer.save(active=True)
                # set active=False for other statuses
                deactivate_other_statuses(instance)

        except Exception as e:
            raise APIException(str(e))


class MLRequestViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
    mixins.UpdateModelMixin,
):
    serializer_class = MLRequestSerializer
    queryset = MLRequest.objects.all()
