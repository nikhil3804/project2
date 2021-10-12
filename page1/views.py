from django.shortcuts import render,redirect
from .models import d1
from django import forms
from .forms import f1, registerForm
from django.contrib import messages
from django.contrib.auth.models import User


#Authentication -> database user exist,
#Authorization -> add, edit   delete x
# Create your views here.
def mypage(request):
    return render(request,'mypage.html')

def show(request):
    sp=d1.objects.all()
    return render(request,'show.html',{'show':sp})

def delete(request,id):
    sp=d1.objects.get(id=id)
    sp.delete()
    return redirect('/mypage/show')


def edit(request,id):
    sp=d1.objects.get(id=id)
    return render(request,'edit.html',{'show1':sp})


def add(request):
    formz=f1((request.POST))
    if(request.method=='POST'):
        if formz.is_valid():
            login=formz.cleaned_data['login']
            password=formz.cleaned_data['password']
            db=d1(login=login,password=password)
            db.save()
            
            return redirect('/mypage/show',)

        else:
            return render(request,'add.html',{'errors':f1.errors})
    else:
        return render(request,'add.html',{'show':f1})


def register(request):
    formz=registerForm((request.POST))
    if(request.method=='POST'):
        if formz.is_valid():
            name=formz.cleaned_data['name']
            email=formz.cleaned_data['email']
            password=formz.cleaned_data['password']
            user = User.objects.create_user(name, email, password)
            return redirect('/mypage/show',)

        else:
            return render(request,'register.html',{'errors':formz.errors})
    else:
        return render(request,'register.html',{'show':formz})



def update(request,id):
    record=d1.objects.get(id=id)
    formz=f1(request.POST)
    if formz.is_valid():
        record.login=formz.cleaned_data['login']
        record.password=formz.cleaned_data['password']
        record.save()
        return redirect('/mypage/show')
    else:
        print("form not submitted",f1.errors)
    
    return render(request,'edit.html',{'showing':record})



    






