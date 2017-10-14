# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect


def checkout(request):
	print '**CHECKOUT**' * 255