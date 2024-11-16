from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class BaseModel(models.Model):
    
    created_date = models.DateTimeField(auto_now_add=True)

    updated_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

class Brand(BaseModel):
    
    name = models.CharField(max_length=200)

    def __str__(self):
        
        return self.name
    
class Size(BaseModel):
    
    size = models.CharField(max_length=100)

    def __str__(self):
        
        return self.name

class Category(BaseModel):
    
    name = models.CharField(max_length=100)

    def __str__(self):
        
        return self.name
    
class Tag(BaseModel):
    
    name = models.CharField(max_length=100)

    def __str__(self):
        
        return self.name
    
class Product(BaseModel):
    
    title = models.CharField(max_length=200)

    description = models.TextField()
    
    price = models.PositiveIntegerField()

    picture = models.ImageField( upload_to="product_images",null = True,blank=True)

    brand_object=models.ForeignKey(Brand,on_delete=models.CASCADE)

    category_object=models.ForeignKey(Category,on_delete=models.CASCADE)

    size_objects=models.ManyToManyField(Size)

    tag_objects=models.ManyToManyField(Tag)

    color=models.CharField(max_length=200)


    def __str__(self):
        
        return self.title
    
class Basket(BaseModel):
    
    owner = models.OneToOneField(User,on_delete=models.CASCADE,related_name="cart")

class BasketItem(BaseModel):

    product_object=models.ForeignKey(Product,on_delete=models.CASCADE)

    quantity=models.PositiveIntegerField(default=1)

    size_object=models.ForeignKey(Size,on_delete=models.CASCADE)

    is_order_placed=models.BooleanField(default=False)

    basket_object=models.ForeignKey(Basket,on_delete=models.CASCADE,related_name="cart_item")
    
    # Query to fetch basket item to authenticated user

    # BasketItem.objects.filter(basket_object__owner=request.user)

    # request.user.cart.cart_item.filter(is_order_placed=False)

    

    
    

    
    
    

    
    