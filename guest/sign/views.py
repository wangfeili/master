from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event

def hello(request):
    return render(request,"hello.html")

def index(request):
    return  render(request,"index.html")

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username = username,password = password)
        if user is not None:
            auth.login(request,user)
            response = HttpResponseRedirect('/event_manage/')
            # response.set_cookie('user',username,3600) #添加浏览器cookie
            request.session['user'] = username #将session记录到浏览器
            return response
        else:
            return render(request,'index.html',{'error':'username or password error!'})

#发布会管理
@login_required()
def event_manage(request):
    event_list = Event.objects.all()
    # username = request.COOKIES.get('user','') #读取浏览器cookie
    username = request.session.get('user','') #读取浏览器session
    return render(request,"event_manage.html",{"user":username,"events":event_list})