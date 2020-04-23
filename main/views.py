from django.shortcuts import render
from django.http import HttpResponse, request
# Create your views here.
def index(request):
	message='done'
	ok='ok'
	return render(request,"home.html",{"message":message,"ok":ok})