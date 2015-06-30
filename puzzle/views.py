from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.base import View
from django.core.context_processors import csrf
from django.contrib.auth import logout as auth_logout
from puzzle.models import *
from os import remove, rename
import json


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



