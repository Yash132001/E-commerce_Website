from django.db import models

# Create your models here.


class Product(models.Model):
    product_id = models.AutoField
    category = models.CharField(max_length=60,default="")
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    Price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/images",default="")


    def __str__(self):
        return self.product_name
        
class Lightbil(models.Model):
    bil_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    meter_no = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70,default="")
    phone = models.CharField(max_length=70,default="")
    desc = models.CharField(max_length=500  ,default="")

    def __str__(self):
        return self.name
    
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=111)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=111, null=True, blank=True)
    city = models.CharField(max_length=222, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    zip_code = models.CharField(max_length=222, null=True, blank=True)
    phone = models.CharField(max_length=111, null=True, blank=True)
    
    def __str__(self):
        return self.name

class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.update_desc[0:7] + "..."
    

    

    
    
