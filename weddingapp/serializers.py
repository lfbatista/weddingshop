from rest_framework import serializers
from weddingapp.models import *


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "brand",
            "price",
            "stock",
            "created",
            "url",
        ]
