from django.contrib import admin
from .models import *


class CharacteristicInline(admin.TabularInline):
    model = Characteristic
    extra = 0

class PhotoInline(admin.TabularInline):
    model = PhotoLaptop
    extra = 0

class LaptopAdmin(admin.ModelAdmin):
    inlines = [CharacteristicInline,PhotoInline]

admin.site.register(Laptop,LaptopAdmin)
admin.site.register(CategoryLaptop)
admin.site.register(BrandLaptop)
