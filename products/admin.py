from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Product, ProductImage, Brand, Review



class ProductAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Brand)
admin.site.register(Review)