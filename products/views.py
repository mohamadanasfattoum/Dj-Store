from django.shortcuts import render
from django.views.generic import ListView , DeleteView
from .models import Product


class ProductList(ListView):
    model = Product


