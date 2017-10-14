# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Order(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField()
	phone_number = models.CharField(max_length=10)
	address = models.CharField(max_length=250)
	city = models.CharField(max_length=100)
	state =models.CharField(max_length=2)
	postal_code = models.IntegerField()
	payment = models.CharField(max_length=255)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)