from rest_framework import serializers
from .models import   Product

class JoinEmployeeToPlace(serializers.Serializer):
    employee_id = serializers.IntegerField()
    place_id = serializers.IntegerField()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name"]
      