from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.base import View
from django.core.context_processors import csrf
from django.contrib.auth import logout as auth_logout
from puzzle.models import *
from os import remove, rename
import json
import random, string

key = 5380971438

def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))

def home(request):
	return render_to_response('1.html')

def helloworld(request):
	args = {}
	args.update(csrf(request))
	return render_to_response('2.html',args)

def last(request):
	if request.POST:
		return render_to_response('3.html')
	else:
		return HttpResponseRedirect('/helloworld/')

#afsdwidadjdhdbdedddj


def getlevel(path):
	number = ""
	for i in range(0, len(path)):
		if i%2 :
			number += path[i]

	string = ""

	for i in number:
		string += str((ord(i) - 97))


	level = int(string)
	level ^= key
	return level

def keepclicking(request, path):

	args = {}

	level = getlevel(path)

	if (level == 5):
		return HttpResponse("done")

	level += 1

	level ^= key

	string = str(level)
	mid = ""

	for i in string:
		mid += chr(int(i) + 97)

	pre = randomword(10)
	newpath = ""
	for i in range(20):
		if not i%2:
			newpath += pre[i/2]
		else:
			newpath += mid[i/2]

	print newpath
	args["next"] = newpath
	args.update(csrf(request))
	
	# return HttpResponseRedirect("/keepclicking/" + newpath)
	return render_to_response('4.html')


