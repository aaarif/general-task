# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from task.models import Users, Friends

class UsersAdmin(admin.ModelAdmin):
	pass
	
class FriendsAdmin(admin.ModelAdmin):
	list_display = ('users', 'friend')

admin.site.register(Users, UsersAdmin)
admin.site.register(Friends, FriendsAdmin)
