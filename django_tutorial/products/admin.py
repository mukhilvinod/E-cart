from django.contrib import admin
from .models import Product,Offer,Offer2,Buy,new_user,new_user1,Buy2



class ProductAdmin(admin.ModelAdmin):
    list_display =('name','price')
class OfferAdmin(admin.ModelAdmin):
    list_display =('code','discount')
class Book(admin.ModelAdmin):
    list_display = ('id','username','email','pincode','phone','job','password')
admin.site.register(new_user, Book)

class node(admin.ModelAdmin):
    list_display = ('id','username','email','phone','country','state','city','landmark','password')

class buyed(admin.ModelAdmin):
    list_display = ('id','name','price','username','email','phone','country','state','city','landmark')


# Register your models here.

admin.site.register(Product,ProductAdmin)
admin.site.register(Offer,OfferAdmin)
admin.site.register(Offer2)
admin.site.register(Buy)
admin.site.register(Buy2,buyed)


admin.site.register(new_user1,node)