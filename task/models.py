# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Users(models.Model):
	name = models.CharField(max_length=30)
	
	def __str__(self):
		return self.name
	
class Friends(models.Model):
	users = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='users')
	friend = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='friend')
