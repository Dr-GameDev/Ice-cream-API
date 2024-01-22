from rest_framework import serializers
from .models import IceCream

class IceCreamSerializer(serializers.ModelSerializer):
    description = serializers.JSONField(default=dict)

    class Meta:
        model = IceCream
        fields = ["id", "name", "description"]
