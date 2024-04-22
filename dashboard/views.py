from rest_framework.views import APIView
from account.models import User
from dashboard.serializers import DashAdminCountSerializer, DashSellerCountSerializer
from orders.models import Order, OrderItem
from products.models import Product, ProductVariant
from rest_framework import status
from rest_framework.response import Response
from datetime import date
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count
from django.db.models import Subquery, OuterRef
from django.db.models import Sum


class AdminDashCountAPIView(APIView):
    def get(self, request, format=None):
        client_count = User.objects.get_count_by_type('client')
        seller_count = User.objects.get_count_by_type('seller')
        products_count = Product.objects.count()
        order_count = Order.objects.count()
        data = {
            'client_count': client_count,
            'seller_count': seller_count,
            'products_count': products_count,
            'order_count': order_count,
        }
        serializer = DashAdminCountSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

from decimal import Decimal
from django.db.models import Sum

class SellerDashCountAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        seller_instance = request.user 
        product_count = Product.objects.filter(seller=seller_instance).count()
        order_count = OrderItem.objects.filter(product_variant__product__seller=seller_instance).count()
        stock_sum = ProductVariant.objects.filter(product__seller=seller_instance).aggregate(stock_sum=Sum('stock'))['stock_sum'] or 0
        orders = Order.objects.filter(orderitem__product_variant__product__seller=seller_instance)
        total_price_sum = Decimal(0)
        for order in orders:
            order_total_price = sum(item.calculate_subtotal() for item in order.orderitem_set.all())
            total_price_sum += order_total_price

        data = {
            'product_count': product_count,
            'order_count': order_count,
            'stock_sum': stock_sum,
            'total_price_sum': total_price_sum,
        }
        
        serializer = DashSellerCountSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
