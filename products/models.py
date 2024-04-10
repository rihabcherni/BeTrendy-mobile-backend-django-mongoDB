from django.db import models
from account.models import User
from project.constant import COLOR_CHOICES, SIZE_CHOICES

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='assets/categorie_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='assets/subcategorie_images/', null=True, blank=True)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200,default="",blank=False)
    description = models.TextField(max_length=1000,default="",blank=False)
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    discount = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    brand = models.CharField(max_length=200,default="",blank=False)
    subcategory = models.ForeignKey(SubCategory, default='', related_name='products', on_delete=models.CASCADE)
    seller = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='assets/product_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    color = models.CharField(max_length=200, choices=COLOR_CHOICES, blank=True) 
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, blank=True)
    stock = models.IntegerField(default=0)

    class Meta:
        unique_together = ('product', 'color', 'size')

    def __str__(self):
        return f"{self.product.name} - Color: {self.color}, Size: {self.size}, Stock: {self.stock}"

class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='assets/product_images/')        

    def __str__(self):
        return self.image
      
class Review(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    rating = models.IntegerField(default=0, choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(max_length=1000,default="",blank=False) 
    createAt = models.DateTimeField(auto_now_add=True) 

    class Meta:
        unique_together = ('product', 'user') 
        
    def __str__(self):
        return f"{self.user.first_name}'s rating ({self.rating}) for {self.product.name}"
    
class Post(models.Model):
    author =models.ForeignKey(User,on_delete=models.CASCADE, default='')
    title = models.CharField(max_length=50)
    body = models.TextField()

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField('Product')
