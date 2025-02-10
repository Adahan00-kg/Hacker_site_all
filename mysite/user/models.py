from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from laptop.models import Laptop
from accessories.models import Accessories


class UserProfile(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(blank=True)


    def __str__(self):
        return f'{self.first_name}- {self.last_name}'




class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE)
    accessories = models.ForeignKey(Accessories, related_name='accessories_item', on_delete=models.CASCADE, null=True, blank=True)
    laptops = models.ForeignKey(Laptop, related_name='laptops_item', on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveSmallIntegerField(default=1)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Товары:{self.cart}'