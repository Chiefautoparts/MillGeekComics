# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
	print '**index**' * 100
	return render(request, 'home/home.html')

def events(request):
	print '**events**' * 100
	return render(request, 'home/events.html')

def magic(request):
	print '**magic**' * 100
	return render(request, 'home/magic.html')