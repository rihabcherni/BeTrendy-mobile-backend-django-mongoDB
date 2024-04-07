from django.urls import path
from project import settings
from django.conf.urls.static import static
from .views import (
    AddOrderAPIView,
    OrderListCreateView,
    OrderRetrieveUpdateDestroyView,
    OrderItemListCreateView,
    OrderItemRetrieveUpdateDestroyView,
)
urlpatterns = [
    path('add-orders/', AddOrderAPIView.as_view(), name='add-order'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyView.as_view(), name='order-retrieve-update-destroy'),
    path('orderitems/', OrderItemListCreateView.as_view(), name='order-item-list-create'),
    path('orderitems/<int:pk>/', OrderItemRetrieveUpdateDestroyView.as_view(), name='order-item-retrieve-update-destroy'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

