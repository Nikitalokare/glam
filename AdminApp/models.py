from django.db import models

# Create your models here.
class Category(models.Model):
    Category_Name = models.CharField(max_length=20)

    def __str__(self):
        return self.Category_Name

    class Meta:
        db_table = 'Category'
        
class Product_Category(models.Model):
    product_cate_name = models.CharField(max_length=100)
    product_cate_quantity = models.FloatField(default=10)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.product_cate_name 

    class Meta:
        db_table = 'Product_Category'

class Brand(models.Model):
    brand_name = models.CharField(max_length=50)

    def __str__(self):
        return self.brand_name

    class Meta:
        db_table = 'Brand'
        
class products(models.Model):
    product_name = models.CharField(max_length=30)
    product_brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    product_price = models.FloatField(default=200)
    product_quantity = models.FloatField(default=20)
    product_desc = models.CharField(max_length=100)
    product_img = models.ImageField(upload_to="Image",default="")
    category = models.ForeignKey(Product_Category,on_delete=models.CASCADE)

    class Meta:
        db_table = "products"

class payment(models.Model):
    card_no = models.CharField(max_length=4)
    cvv =  models.CharField(max_length=4)
    expiry =  models.CharField(max_length=10)
    balance = models.FloatField(default=10000)

    class Meta:
        db_table = "Payment"