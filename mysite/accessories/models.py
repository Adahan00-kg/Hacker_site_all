from django.db import models


class CategoryAccessories(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.category}'

class BrandAccessories(models.Model):
    brand = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.brand}'

class Accessories(models.Model):
    category = models.ForeignKey(CategoryAccessories, related_name='category_access', on_delete=models.CASCADE)
    brand  = models.ForeignKey(BrandAccessories, related_name='brand_access', on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    price = models.PositiveSmallIntegerField(null=True, blank=True)
    available = models.BooleanField(default=True)
    accessor_discount = models.PositiveSmallIntegerField(null=True,blank=True,help_text='процент скидки')
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.name} - {self.price}'


class AccessIMG(models.Model):
    accessories = models.ForeignKey(Accessories, related_name='img_accessories', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='img_accessories/', null=True, blank=True)
    color= models.CharField(max_length=100)

    def __str__(self):
        return f'{self.accessories} - {self.color}'


class ParameterAccess(models.Model):
    accessories = models.ForeignKey(Accessories, related_name='accessories', on_delete=models.CASCADE)
    parameter = models.CharField(max_length=500)
    value_parameter = models.TextField(null=True, blank=True)


    
