from django.urls import path
from project import settings
from django.conf.urls.static import static
from .views import (
    ProductImagesListCreateView,
    ProductImagesRetrieveUpdateDestroyView,
    ProductVariantListCreateView,
    ProductVariantRetrieveUpdateDestroyView,
    SubCategoryListCreateView,
    SubCategoryRetrieveUpdateDestroyView,
    WishlistListCreateAPIView,
    WishlistRetrieveUpdateDestroyAPIView,
    get_products_by_category,
    get_subcategories_by_category,
    home,
    CategoryListCreateView,
    CategoryRetrieveUpdateDestroyView,
    ProductListCreateView,
    ProductRetrieveUpdateDestroyView,
    ReviewListCreateView,
    ReviewRetrieveUpdateDestroyView,
    PostListCreateView,
    PostRetrieveUpdateDestroyView,
)
urlpatterns = [
    path('', home, name='home'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-retrieve-update-destroy'),
   
    path('subcategories/', SubCategoryListCreateView.as_view(), name='subcategory-list-create'),
    path('subcategories/<int:pk>/', SubCategoryRetrieveUpdateDestroyView.as_view(), name='subcategory-retrieve-update-destroy'),
   
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-retrieve-update-destroy'),

    path('products-variants/', ProductVariantListCreateView.as_view(), name='product-variants-list-create'),
    path('products-variants/<int:pk>/', ProductVariantRetrieveUpdateDestroyView.as_view(), name='product-variants-retrieve-update-destroy'),

    path('products-iamges/', ProductImagesListCreateView.as_view(), name='product-iamges-list-create'),
    path('products-iamges/<int:pk>/', ProductImagesRetrieveUpdateDestroyView.as_view(), name='product-iamges-retrieve-update-destroy'),

    path('product/<str:category_name>/', get_products_by_category, name='products-by-category'),
    path('product/<str:category_name>/<str:subcategory_name>/', get_products_by_category, name='products-by-subcategory'),

    path('subcategories/<str:category_name>/', get_subcategories_by_category, name='subcategories-by-category'),

    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='review-retrieve-update-destroy'),
    
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-retrieve-update-destroy'),
 
    path('wishlist/', WishlistListCreateAPIView.as_view(), name='wishlist-list-create'),
    path('wishlist/<int:pk>/', WishlistRetrieveUpdateDestroyAPIView.as_view(), name='wishlist-detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
