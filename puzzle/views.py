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

	
	args["message"] = ""

	if request.method == "POST":
		found = 0
		for i in password.objects.all():
			if i.key == request.POST["hash"]:
				found = 1
				if i.state == 0:
					args["message"] = "Oh you shrewd guy. How did you? Mail me @ kushagra14056@iiitd.ac.in"
					return render_to_response('1.html', args)
				elif i.state == 1:
					return HttpResponseRedirect("/doge")
				elif i.state == 2:
					args["message"] = "This hash has already been claimed"
					return render_to_response("1.html", args)

		if not found:
			args["message"] = "Wrong hash BRO"
			return render_to_response("1.html", args)

	return render_to_response('1.html', args)
	
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

	if (level == 616):
		found = 0
		passkey = ""

		for i in password.objects.all():
			if i.state == 0:
				found = 1
				i.state = 1
				i.save()
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

def validate(email1, email2, email3, email4):
	allreg = Registration.objects.all()
	ct = 0
	for i in allreg:
		e = [i.email1,i.email2,i.email3,i.email4]
		if email1 in e:
			return email1
		if email2 in e:
			return email2
		if email3 in e:
			return email3
		if email4 in e:
			return email4

	return 1


def register(request):
	args = {}
	args["message"] = ""

	if request.method == 'POST':
		teamname = request.POST['teamname']
		key = request.POST['key']
		name1 = request.POST['name1']
		email1 = request.POST['email1']
		git1 = request.POST['git1']
		ph1 = request.POST['ph1']
		name2 = request.POST['name2']
		email2 = request.POST['email2']
		git2 = request.POST['git2']
		ph2 = request.POST['ph2']
		name3 = request.POST['name3']
		email3 = request.POST['email3']
		git3 = request.POST['git3']
		ph3 = request.POST['ph3']
		name4 = request.POST['name4']
		email4 = request.POST['email4']
		git4 = request.POST['git4']
		ph4 = request.POST['ph4']

		try:
			p = password.objects.get(key=key)
		except:
			args["message"] = "Invalid key!"
			args.update(csrf(request))
			return render_to_response('register.html',args)

		if p.state == 2:
			args["message"] = "Key already used!"
			args.update(csrf(request))
			return render_to_response('register.html',args)

		if p.state == 0:
			args["message"] = "You shrewd guy! Play fairly"
			args.update(csrf(request))
			return render_to_response('register.html',args)

		ans = validate(email1,email2,email3,email4)

		if(ans != 1):
			args["message"] = ans + " has already registered in another team"
			args.update(csrf(request))
			return render_to_response('register.html',args)

		reg = Registration(teamname=teamname,key=p,name1=name1,email1=email1,git1=git1,ph1=ph1,name2=name2,email2=email2,git2=git2,ph2=ph2,name3=name3,email3=email3,git3=git3,ph3=ph3,name4=name4,email4=email4,git4=git4,ph4=ph4)
		reg.save()
		p.state = 2
		p.save()
		args["message"] = "Registration successful"
		args.update(csrf(request))
		return render_to_response('register.html',args)

	else:
		args.update(csrf(request))
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
