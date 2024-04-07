from rest_framework import serializers

class DashAdminCountSerializer(serializers.Serializer):
    client_count = serializers.IntegerField()
    seller_count = serializers.IntegerField()
    products_count = serializers.IntegerField()
    order_count = serializers.IntegerField()



class DashSellerCountSerializer(serializers.Serializer):
    product_count = serializers.IntegerField()
    order_count = serializers.IntegerField()
