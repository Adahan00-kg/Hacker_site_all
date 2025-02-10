from django.contrib import admin
from .models import *



class AccessIMGInlines(admin.TabularInline):
    model = AccessIMG
    extra = 0

class ParameterAInlines(admin.TabularInline):
    model = ParameterAccess
    extra = 0


class AccessAdmin(admin.ModelAdmin):
    inlines = [AccessIMGInlines,ParameterAInlines]

admin.site.register(Accessories, AccessAdmin)
admin.site.register(CategoryAccessories)
admin.site.register(BrandAccessories)