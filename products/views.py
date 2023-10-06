from typing import Any
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Product , Brand


class ProductList(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product


class BrandList(ListView):
    model = Brand


class BrandDetail(ListView):
    model = Product
    template_name = 'products/brand_detail.html'

    
    def get_queryset(self):
        queryset = super(BrandDetail, self).get_queryset()
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        queryset = queryset.filter(brand=brand)
        return queryset
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['brand'] = Brand.objects.get(slug=self.kwargs['slug'])
        return context