from django.urls import path
from project import settings
from django.conf.urls.static import static
from .views import (
    PaymentInfoListCreateView,
    PaymentInfoRetrieveUpdateDestroyView,
)
urlpatterns = [
    path('payment/', PaymentInfoListCreateView.as_view(), name='payment-info-list-create'),
    path('payment/<int:pk>/', PaymentInfoRetrieveUpdateDestroyView.as_view(), name='payment-info-detail'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

