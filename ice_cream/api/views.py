from django.http import JsonResponse
from .models import IceCream
from .serializers import IceCreamSerializer

def index(request):
    ice_cream = IceCream.objects.all()
    serializer = IceCreamSerializer(ice_cream, many=True)
    print(serializer.data)  # Add this line to inspect the serialized data
    return JsonResponse({"ice creams": serializer.data}, safe=False)
