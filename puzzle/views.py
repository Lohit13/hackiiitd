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
from .forms import RegForm

key = 5380971438

def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))

def home(request):
	args = {}
	args.update(csrf(request))
	args['form'] = RegForm()
	num = 0

	for i in password.objects.all():
		if i.state == 0:
			num += 1

	args["left"] = num
	print num

	return render_to_response('register.html', args)
	
def check(request):

	found = 0

	for i in password.objects.all():
		if i.key == request.POST["keyval"] and i.state == 0:
			found = 1
			break

	if found == 1:
		return HttpResponse("yay")
	else:
		return HttpResponse("nay")



def helloworld(request):
	args = {}
	args.update(csrf(request))
	return render_to_response('2.html',args)

def last(request):
	if request.POST:
		return HttpResponseRedirect('/keepclicking/')
	else:
		return HttpResponseRedirect('/helloworld/')


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
	args.update(csrf(request))

	args["next"] = "afsdwidadjdhdbdedddj"

	if request.method == "GET":
		return HttpResponseRedirect("/")
	elif request.method == "POST" and len(path) < 20:
		print "here"
		return render_to_response('4.html', args)

	print path
	level = getlevel(path)

	if (level == 3):
		found = 0
		passkey = ""

		for i in password.objects.all():
			if i.state == 0:
				found = 1
				i.state = 1
				# i.save()		not saving beacause in dev mode
				passkey = i.key
				break

		if found:
			string = "your key is " + passkey
		else:
			string = "sorry, keys are over"

		return HttpResponse(string)

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

	# return HttpResponseRedirect("/keepclicking/" + newpath)
	return render_to_response('4.html', args)

def register():
	if request.method == 'POST':
		return HttpResponse('some')
	else:
		args = {}
		args.update(csrf(request))
		args['form'] = RegForm()
		return render_to_response('register.html',args)


def generate(request):

	for i in range(500):
		psw = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase  + string.digits) for _ in range(15))
		ct = password.objects.filter(key=psw).count()
		if ct==0 :
			p = password(key=psw)
			p.save()
		else:
			pass

	return HttpResponse(password.objects.all().count())




