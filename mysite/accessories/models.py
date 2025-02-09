from django.db import models


class Accessories(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    price = models.PositiveSmallIntegerField(null=True, blank=True)
    available = models.BooleanField(default=True)
    dop_title = models.CharField(max_length=300, null=True, blank=True)
    dop_description1 = models.TextField(null=True, blank=True)
    dop_description2 = models.TextField(null=True, blank=True)
    dop_description3 = models.TextField(null=True, blank=True)


    def __str__(self):
        return f'{self.name} - {self.price}'


class AccessIMG(models.Model):
    accessories = models.ForeignKey(Accessories, related_name='img_accessories', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='img_accessories/', null=True, blank=True)



class ParameterAccess(models.Model):
    accessories = models.ForeignKey(Accessories, related_name='accessories', on_delete=models.CASCADE)
    parameter = models.CharField(max_length=500)
    value_parameter = models.TextField(null=True, blank=True)


    
