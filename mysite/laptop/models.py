from django.db import models

class CategoryLaptop(models.Model):
    category_name = models.CharField(max_length=100,unique=True)


    def __str__(self):
        return f'{self.category_name}'

class BrandLaptop(models.Model):
    brand_name = models.CharField(max_length=150,unique=True)


    def __str__(self):
        return f'{self.brand_name}'


class Laptop(models.Model):
    laptop_name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(CategoryLaptop,on_delete=models.CASCADE,related_name='category_laptop')
    brand = models.ForeignKey(BrandLaptop,on_delete=models.CASCADE,related_name='brand_laptop')
    laptop_discount = models.PositiveSmallIntegerField(null=True,blank=True,help_text='процент скидки')
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.laptop_name} - {self.price}'


class Characteristic(models.Model):
    characteristic_title = models.CharField(max_length=100)
    characteristic_description = models.TextField(null=True,blank=True)
    laptop_connect = models.ForeignKey(Laptop,on_delete=models.CASCADE,related_name='characteristic_laptop')


    def __str__(self):
        return f'{self.characteristic_title} - {self.laptop_connect}'


class PhotoLaptop(models.Model):
    img = models.FileField(upload_to='laptop_photo/')
    color = models.CharField(max_length=150)
    laptop_connect = models.ForeignKey(Laptop,on_delete=models.CASCADE,related_name='photo_laptop')


    def __str__(self):
        return f'{self.laptop_connect} - {self.color}'
