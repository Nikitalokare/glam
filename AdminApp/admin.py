from django.contrib import admin
from .models import products,Product_Category,Category,Brand,payment

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','Category_Name')

class Product_CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','product_cate_name','product_cate_quantity','category')

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id','brand_name')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','product_name','product_brand','product_price','product_quantity','product_desc','product_img','category')

class paymentAdmin(admin.ModelAdmin):
    list_display = ("id","card_no","cvv","expiry","balance")

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product_Category,Product_CategoryAdmin)
admin.site.register(products,ProductAdmin)
admin.site.register(Brand,BrandAdmin)
admin.site.register(payment,paymentAdmin)