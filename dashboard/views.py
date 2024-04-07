from rest_framework.views import APIView
from account.models import User
from dashboard.serializers import DashAdminCountSerializer, DashSellerCountSerializer
from orders.models import Order, OrderItem
from products.models import Product
from rest_framework import status
from rest_framework.response import Response
from datetime import date
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count
from django.db.models import Subquery, OuterRef


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

class SellerDashCountAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        seller_instance = request.user 
        
        product_count = Product.objects.filter(seller=seller_instance).count()
        order_count = OrderItem.objects.filter(product_variant__product__seller=seller_instance).count()
        data = {
            'product_count': product_count,
            'order_count': order_count,
        }
        
        serializer = DashSellerCountSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)