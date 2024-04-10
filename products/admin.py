from django.contrib import admin

from products.models import Category,Post,Product, ProductImages, ProductVariant,Review, SubCategory, Wishlist

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(ProductVariant)
admin.site.register(ProductImages)
admin.site.register(Review)
admin.site.register(Post)
admin.site.register(Wishlist)

