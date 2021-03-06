from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as login_user,logout as logout_user
from .forms import Loginform,Signupform

def login(request):
    if request.method=='POST':
        form = Loginform(request.POST)
        username = form.data['username']
        password= form.data['password']
        if authenticate(username=username,password=password):
            user=User.objects.get(username=username)
            login_user(request,user)
            context = {'loginform':user}
            return render(request,'base.html',context)
        else:
            return HttpResponseRedirect('/signup')
    else:
        loginform=Loginform()
        context={'loginform':loginform}
        return render(request,'base.html',context)

def signup(request):

    if request.method=='POST':
        form=Signupform(request.POST)
        username = form.data['username']
        password = form.data['password']
        cPassword = form.data['confirm_password']
        email = form.data['email']
        firstname = form.data['firstname']
        lastname = form.data['lastname']
        if len(User.objects.filter(username=username)) ==0:
            try:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname)
                user.save()
            except Exception as a:
                messages.error(request,f"{a}")
            else:
                messages.info(request,f"{username} ,User Successfully created")
            loginform = Loginform()
            context = {'loginform': loginform}
            return render(request,'base.html',context=context)
        else:
            messages.error(request,"user Name laready exits")
            if password!=cPassword:
                messages.error(request, "pass word does not match")
            signupform = Signupform()
            context = {'signupform': signupform}
            return render(request, 'base.html', context)

    else:
        signupform=Signupform()
        context={'signupform':signupform}
        return render(request,'base.html',context)


def logout(request):
    logout_user(request)
    return HttpResponseRedirect('/')

