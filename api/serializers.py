from rest_framework import serializers
from .models import Store, Product


class StoreSerializer(serializers.ModelSerializer):
    create_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    class Meta:
        model = Store
        fields = ['store_id', 'store_location', 'created_at', 'updated_at']

class ProductSerializer(serializers.ModelSerializer):
    created_att = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_att = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    class Meta:
        model = Product
        fields = ['product_id', 'product_name', 'created_att', 'updated_att']