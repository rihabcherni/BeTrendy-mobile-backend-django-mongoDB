from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from products.models import Category, Post, Product, ProductImages, ProductVariant, Review, SubCategory, Wishlist
from .serializers import  CategorySerializer, PostSerializer, ProductImagesSerializer, ProductSerializer, ProductVariantSerializer, ReviewSerializer, SubCategorySerializer, WishlistSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

def home(request):
    return HttpResponse("Welcome to the Shopee backend!")  

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryListCreateView(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class SubCategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductVariantListCreateView(generics.ListCreateAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer

class ProductVariantRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer


class ProductImagesListCreateView(generics.ListCreateAPIView):
    queryset = ProductImages.objects.all()
    serializer_class = ProductImagesSerializer

class ProductImagesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductImages.objects.all()
    serializer_class = ProductImagesSerializer



class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def get_products_by_category(request, category_name, subcategory_name=None):
    subcategory = get_object_or_404(SubCategory, name=subcategory_name, category__name=category_name) if subcategory_name else None
    products = Product.objects.filter(subcategory=subcategory) if subcategory else Product.objects.filter(subcategory__category__name=category_name)
    serializer = ProductSerializer(products, many=True, context={'request': request})
    return JsonResponse(serializer.data, safe=False)

def get_subcategories_by_category(request, category_name):
    subcategories = SubCategory.objects.filter(category__name=category_name)
    data = [{
        'id': subcategory.id,
        'category_name': subcategory.category.name,
        'name': subcategory.name,
        'description': subcategory.description,
        'image': subcategory.image.url if subcategory.image else None,
    } for subcategory in subcategories]
    return JsonResponse(data, safe=False)


class WishlistListCreateAPIView(generics.ListCreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

class WishlistRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
