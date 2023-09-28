from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from taggit.managers import TaggableManager

FLAG_CHOTCES = (
    ('Sale','Sale'),
    ('Feature','Feature'),
    ('New','New'),
)

class Product(models.Model):
    name = models.CharField(_('Name'), max_length=120)
    image = models.ImageField(_('Image'), upload_to= 'product')
    price = models.FloatField(_('Price'))
    flag = models.CharField(_('Flag'),max_length=10, choices=FLAG_CHOTCES)
    brand = models.ForeignKey('Brand',verbose_name=_('Brand'), related_name='product_brand', on_delete=models.SET_NULL, null=True, blank=True )
    sku = models.CharField(_('SKU'),max_length=10)
    subtitle = models.TextField(_('Subtitle'), max_length=500)
    description = models.TextField(_('Description'), max_length=1000)
    quantity = models.IntegerField(_('Quantity'))
    tags = TaggableManager()




class ProductImage(models.Model):
    product =models.ForeignKey(Product, on_delete=models.CASCADE , related_name='product_image')
    image = models.ImageField(_("Image"), upload_to='product_images')


class Brand(models.Model):
    name = models.CharField(_('Name'), max_length=120)
    image = models.ImageField(_('Image'), upload_to= 'brands')
    slug = models.SlugField(null=True, blank=True)

class Review(models.Model):
    user = models.ForeignKey(User, related_name= 'review_user',on_delete=models.SET_NULL, null=True, blank=True)#If delete User, not delete the comment
    product = models.ForeignKey(Product, related_name='product_review', on_delete=models.CASCADE) #If delete the product,delete the comment
    review = models.TextField(_('Name'), max_length=500)
    rate = models.ImageField()
    created_at = models.DateTimeField(default=timezone.now)
    

