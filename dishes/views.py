from django.db.models import Prefetch
from rest_framework.viewsets import ModelViewSet

from dishes.models import FoodCategory, Food
from dishes.serializers import FoodListSerializer


class FoodView(ModelViewSet):
    serializer_class = FoodListSerializer
    queryset = FoodCategory.objects.prefetch_related(
        Prefetch('food', queryset=Food.objects.filter(is_publish=True))
    )
