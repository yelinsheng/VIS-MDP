# coding=utf-8

from django.http import HttpResponse
from django.shortcuts import render
from MDP.ComputeEngine import ComputeEngine
import json

def index(request):
	#return HttpResponse("Hello world ! ")
	return render(request, 'index.html')

def computeDepthJson(request):
	request.encoding = 'utf-8'
	if 'reward' in request.GET:
		reward = request.GET['reward'].encode('utf-8')
		computeEngine = ComputeEngine(reward)
		depth2 = computeEngine.computeDepth2()
		return HttpResponse(depth2)
	else:
		return HttpResponse("failed")



def computeTableJson(request):
	request.encoding = 'utf-8'
	if 'reward' in request.GET:
		reward = request.GET['reward'].encode('utf-8')
		computeEngine = ComputeEngine(reward)
		table = computeEngine.computeTable()
		return HttpResponse(table)
	else:
		return HttpResponse("failed")



