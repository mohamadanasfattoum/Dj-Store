from django.db import models

class Product(models.Model):
    name = models.CharField(_('Name'), max_length=120)