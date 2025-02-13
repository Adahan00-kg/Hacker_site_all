from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator
from laptop.models import Laptop,PhotoLaptop
from accessories.models import Accessories


class UserProfile(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(blank=True)


    def __str__(self):
        return f'{self.first_name}  - {self.last_name}'






class Rating(models.Model):
    user = models.ForeignKey(UserProfile, related_name='ratings', on_delete=models.CASCADE)
    accessor = models.ForeignKey(Accessories, related_name='access_rating', on_delete=models.CASCADE)
    laptop = models.ForeignKey(Laptop, related_name='laptop_rating', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField([MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True)
    comment = models.TextField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user} -  {self.accessor or self.laptop}'


class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE)
    accessories = models.ForeignKey(Accessories, related_name='accessories_item', on_delete=models.CASCADE, null=True, blank=True)
    laptop_img = models.ForeignKey(PhotoLaptop,on_delete=models.CASCADE,null=True,blank=True)
    laptops = models.ForeignKey(Laptop, related_name='laptop_item', on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveSmallIntegerField(default=1)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Товары:{self.cart}'