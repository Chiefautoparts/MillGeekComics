# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm

# Create your views here.
def product_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	if category_slug:
		categeory = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)
	return render(request,
						'catalog/product/list.html',
						{'category': category,
						'category': categories,
						'products': products})

def product_details(request, id, slug):
	product = get_object_or_404(Product,
								id=id,
								slug=slug,
								available=True)
	cart_product_form = CartAddProductForm()
	return render(request, 'catalog/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})