from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.base import View
from django.contrib.auth import logout as auth_logout
from puzzle.models import *
from os import remove, rename
import json


def home(request):
	f  = open("passes.txt", "r")
	a = f.readlines()

	b = []

	for i in range(0, len(a)):
		b.append(a[i].strip("\n"));

	for i in b:
		newpass = password(key = i)
		newpass.save()

	return HttpResponse("ok")