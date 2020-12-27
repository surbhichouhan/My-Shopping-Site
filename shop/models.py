from django.db import models

# Create your models here.

class Product(models.Model):
   
    product_id  =  models.AutoField
    product_name  =  models.CharField(max_length=50)
    price = models.IntegerField()
    desc  = models.CharField(max_length=300)
    pub_date  =  models.CharField(max_length=50)
    category = models.CharField(max_length=50 ,default="")
    sub_category =models.CharField(max_length=50,default="")
    image = models.ImageField(upload_to="shop/images" , default="")


    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_Id =  models.AutoField(primary_key=True)
    name  =  models.CharField(max_length=50 )
    email =  models.CharField(max_length=70)
    desc  = models.CharField(max_length=500)
    phone = models.CharField(max_length=50,default='')

    def __str__(self):
        return self.name

class Order(models.Model):
    order_Id =  models.AutoField(primary_key=True)
    itemJson = models.CharField(max_length=500 )
    name  =  models.CharField(max_length=50 )
    email =  models.CharField(max_length=90)
    state =  models.CharField(max_length=70)
    Zip =  models.CharField(max_length=70)
    city =  models.CharField(max_length=70)
    address  = models.CharField(max_length=100)
    phone = models.CharField(max_length=50,default='')

    
class OrderUpdate(models.Model):
    update_Id =  models.AutoField(primary_key=True)
    order_Id =  models.IntegerField(default="")
    updae_desc = models.CharField(max_length=500 )
    timestamp  =  models.DateField(auto_now_add=True)
   
def __str__(self):
    return self.updae_desc[0:7]+"......."

