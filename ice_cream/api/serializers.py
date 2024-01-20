from rest_framework import serializers
from .models import IceCream

class IceCreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = IceCream
        fields = ["id", "name", "description"]
        extra_kwargs = {
            "description": {"origin": "", "flavors": [], "toppings": []}
        }
