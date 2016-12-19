# coding=utf-8

from django.http import HttpResponse
from django.shortcuts import render
from MDP.ComputeEngine import ComputeEngine
import json

def index(request):
	#return HttpResponse("Hello world ! ")
	return render(request, 'index.html')

def computeDepthJson(request):
	computeEngine=ComputeEngine()
	depth2=computeEngine.computeDepth2()
	print depth2
	result=""
	result += json.dumps(depth2)
	return HttpResponse(depth2)

def computeTableJson(request):
	computeEngine = ComputeEngine()
	table = computeEngine.computeTable()
	return HttpResponse(table)

