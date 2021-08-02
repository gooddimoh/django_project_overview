from django.contrib import admin
from .models import *



admin.site.register([
    Product,
    ProductType,
    ProductCategory,
    Standard,
    StandardCategory,
    StandardRequirement,
    KeyWords,
])