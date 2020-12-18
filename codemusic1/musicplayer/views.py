from django.shortcuts import render,redirect
from django.http import HttpResponse
from musicplayer.models import songs
from django.core import serializers
from django.contrib.auth.models import auth
import json
import requests
# Create your views here.
def home(request):
    return render(request ,'musicplayer/home.html') 
def song(request):
    v1 =request.GET['search']
    
    response = requests.get('https://codemusic.vercel.app/search?query='+v1)
    geodata = response.json() 
    print(response)
    return HttpResponse( response, content_type='application/json')
    #return render(request,'musicplayer\\songs.html',{'data':geodata})
def logout(request):
    auth.logout(request)
    return redirect('/')
def like(request):
    render(request , "hello")
def api(request):
    # data=songs.objects.get(musicID=request.GET['id'])
    # print(data.musicIMG)
    # datas=list(data.musicIMG)
    data=request.GET['id']
    sc=songs.objects.filter(musicID__exact=data)
    if(sc.count()>0):
        print("exist")
        datas = serializers.serialize('json',songs.objects.all().filter(musicID__exact=data))
        return HttpResponse( datas, content_type='application/json')
    # else:
    #     response = requests.get('https://codemusic.vercel.app/song?id='+data)
    #     songcred =response.json()
    #     obj=songs(musicID=songcred['id'], musicTitle=songcred['song'], musicDESC=songcred['primary_artists'],musicIMG=songcred['image'],musicUrl=songcred['media_url'])
    #     obj.save()
    #     datas = serializers.serialize('json',songs.objects.all().filter(musicID__exact=data))
    #     return HttpResponse( datas, content_type='application/json')
    #     