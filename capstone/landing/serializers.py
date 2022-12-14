from rest_framework import serializers
from landing.models import buildings
from landing.models import MLAlgorithm
from landing.models import MLAlgorithmStatus
from landing.models import MLRequest


class buildingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = buildings
        fields = "__all__"


class MLAlgorithmSerializer(serializers.ModelSerializer):

    current_status = serializers.SerializerMethodField(read_only=True)

    def get_current_status(self, mlalgorithm):
        return (
            MLAlgorithmStatus.objects.filter(parent_mlalgorithm=mlalgorithm)
            .latest("created_at")
            .status
        )

    class Meta:
        model = MLAlgorithm
        read_only_fields = (
            "id",
            "name",
            "description",
            "code",
            "version",
            "owner",
            "created_at",
            "parent_endpoint",
            "current_status",
        )
        fields = read_only_fields


class MLAlgorithmStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLAlgorithmStatus
        read_only_fields = ("id", "active")
        fields = (
            "id",
            "active",
            "status",
            "created_by",
            "created_at",
            "parent_mlalgorithm",
        )


class MLRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLRequest
        read_only_fields = (
            "id",
            "input_data",
            "full_response",
            "response",
            "created_at",
            "parent_mlalgorithm",
        )
        fields = (
            "id",
            "input_data",
            "full_response",
            "response",
            "feedback",
            "created_at",
            "parent_mlalgorithm",
        )
