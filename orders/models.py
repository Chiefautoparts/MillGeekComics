# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from catalog.models import Product

# Create your models here.
class Order(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField()
	address = models.CharField(max_length=250)
	city = models.CharField(max_length=100)
	postal_code = models.IntegerField(max_length=20)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	paid = models.BooleanField(default=False)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return 'Order {}'.format(self.id)

	def get_total_cost(self):
		return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
	order = models.ForeignKey(Order, related_name='items')
	product = models.ForeignKey(Product, related_name='order_items')
	price = models.DecimalField(max_digits=10, decimal_places=2)
	quantity = models.PositiveIntegerField(default=1)

	def __str__(self):
		return '{}'.format(self.id)

	def get_cost(self):
		return self.price * self.quantity