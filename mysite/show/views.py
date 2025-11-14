from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(req):
    return HttpResponse("大家好，我是李艾嬣")
def about_me(req):
    return render(req,"hello.html")