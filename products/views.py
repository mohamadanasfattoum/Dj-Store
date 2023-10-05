from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Product , Brand


class ProductList(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product


class BrandList(ListView):
    model = Brand


class BrandDetail(DetailView):
    model = Brand