# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from task.models import Users, Friends
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

# Create your views here.
def user(request, user_id):
	try:
		user = Users.objects.get(id=user_id)
		getFriends = Friends.objects.filter(users=user)
		friends = []
		
		for i in getFriends:
			friends.append(i.friend.id)
		
		data = {'id':user.id, 'name':user.name, 'friends':friends}
	except ObjectDoesNotExist:
		data = {'error':'not found'}
		
	return JsonResponse(data)
