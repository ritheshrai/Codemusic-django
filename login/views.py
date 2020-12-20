from django.shortcuts import render
from django.contrib.auth.models import User , auth
from django.http import HttpResponse
import json
from django.shortcuts import redirect
from django.core import serializers
from musicplayer.models import songs,music,playlist, playlistCON


# Create your views here.
def index(request):
     return render(request ,'login/index.html') 
def signin(request):
     if request.method =='POST':
          username=request.POST['username']
          password=request.POST['password']
          user =auth.authenticate(username=username,password=password)
          if user is not None:
               auth.login(request,user)
               return redirect('dashboard/')
          else:
               return render(request,'login/loginerror.html',{'result':'invalid credentials'})

     else:
          redirect('/') 


def list_to_str(item):
    listToStr = ' '.join(map(str, item)) 
    return listToStr  




def register(request):
     if request.method == 'POST':
          username = request.POST['username']
          firstname =request.POST['first-name']
          lastname =request.POST['last-name']
          email = request.POST['email']
          pass1 = request.POST['pass1']
          pass2 = request.POST['pass2']
          if email!='' and pass1!='' and username!='' and firstname!='':
               if pass1==pass2:
                    if User.objects.filter(username=username).exists():
                         return render(request,'login/login.html',{'result':'username taken'})
                         
                    elif User.objects.filter(email=email).exists():
                    
                         return render(request,'login/login.html', {'result':'email already exists'})
                    else:
                         user =User.objects.create_user(username= username,email=email,password=pass1,first_name=firstname,last_name=lastname)
                         user.save() 
                         
                         return render(request,'login/login.html', {'result':'regesterred successful please login using your credentials'})
                        # return redirect('dashbord/')   
               else:
                     return render(request,'login/login.html', {'result':'passwords not matching'})

          else:
               return render(request,'login/login.html', {'result':'fill all the blocks properly'})
     else:
          return render(request,'login/index.html')