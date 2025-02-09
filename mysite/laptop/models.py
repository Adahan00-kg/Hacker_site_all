from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100,unique=True)


class Brand(models.Model):
    brand_name = models.CharField(max_length=150,unique=True)


class Laptop(models.Model):
    laptop_name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='laptop')
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,related_name='brand')
    laptop_discount = models.PositiveSmallIntegerField(null=True,blank=True,help_text='процент скидки')




class PhotoLaptop(models.Model):
    img = models.FileField(upload_to='laptop_photo/')
    color = models.CharField(max_length=150)
    laptop_connect = models.ForeignKey(Laptop,on_delete=models.CASCADE,related_name='color')


