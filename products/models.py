from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _




class Product(models.Model):
    name = models.CharField(_('Name'), max_length=120)
    image = models.ImageField(_('Image'), upload_to= 'product')
    price = models.FloatField()
    



class ProductImage(models.Model):
    product =models.ForeignKey(Product, on_delete=models.CASCADE , related_name='product_image')
    image = models.ImageField(_("Image"), upload_to='product_images')


class Review(models.Model):
    user = models.ForeignKey(User, related_name= 'review_user',on_delete=models.SET_NULL, null=True, blank=True)#If delete User, not delete the comment
    product = models.ForeignKey(Product, related_name='product_review', on_delete=models.CASCADE) #If delete the product,delete the comment
    review = models.TextField(_('Name'), max_length=500)
    rate = models.ImageField()
    created_at = models.DateTimeField(default=timezone.now)
    

