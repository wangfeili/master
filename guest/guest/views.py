from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return render(request,"hello.html")

def index(request):
    return  render(request,"index.html")

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if username == 'admin' and password == 'admin123':
            return HttpResponse('login success!')
        else:
            return render(request,'index.html',{'error':'username or password error!'})