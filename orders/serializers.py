from rest_framework import serializers
from orders.models import  Order, OrderItem
        
class OrderItemSerializer(serializers.ModelSerializer):
    subtotal_price = serializers.SerializerMethodField()
    class Meta:
        model = OrderItem
        fields = '__all__'

    def get_subtotal_price(self, obj):
        return obj.calculate_subtotal()
    
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

