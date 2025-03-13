from rest_framework import viewsets
from api.models import DrinkOrder
from api.serializers import DrinkOrderSerializer, DrinkOrderCreateSerializer

class DrinkOrderViewSet(viewsets.ModelViewSet):
    queryset = DrinkOrder.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return DrinkOrderCreateSerializer
        return DrinkOrderSerializer
