from django.http import HttpResponse
from django.shortcuts import render
import random
# Create your views here.
def password(request):
    thepass=""
    alphabets="abcdefghijklmnopqrstuvwxyz"
    lst=list(alphabets)
    len=request.GET.get('length',12)
    len=int(len)
    if request.GET.get('caps')=="on":
        lst.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if request.GET.get('special')=="on":
        lst.extend('!@#$%^&*')
    if request.GET.get('numbers')=="on":
        lst.extend("0123456789")
    for i in range(len):
        thepass+=random.choice(lst)
    return render(request,'generator/password.html',{'password':thepass})
def home(request):
    return render(request,'generator/home.html')
def about(request):
    return render(request,'generator/about.html')