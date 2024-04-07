from django.urls import path
from dashboard.views import AdminDashCountAPIView, SellerDashCountAPIView
from project import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin-count/', AdminDashCountAPIView.as_view(), name='admin-dash-count'),
    path('seller-count/', SellerDashCountAPIView.as_view(), name='seller-dash-count'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

