from django.urls import path
from project import settings
from django.conf.urls.static import static
from .views import (
    CartListCreateView,
    CartRetrieveUpdateDestroyView,
    CartItemListCreateView,
    CartItemRetrieveUpdateDestroyView,
)
urlpatterns = [
    path('carts/', CartListCreateView.as_view(), name='cart-list-create'),
    path('carts/<int:pk>/', CartRetrieveUpdateDestroyView.as_view(), name='cart-retrieve-update-destroy'),

    path('cartitems/', CartItemListCreateView.as_view(), name='cart-item-list-create'),
    path('cartitems/<int:pk>/', CartItemRetrieveUpdateDestroyView.as_view(), name='cart-item-retrieve-update-destroy'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

