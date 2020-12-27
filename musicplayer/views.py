from django.shortcuts import render,redirect
from django.http import HttpResponse
from musicplayer.models import songs
from django.core import serializers
from django.contrib.auth.models import auth
import json
import requests
#funtionality
import ast 

def to_dict(item):  
    # initializing string  
    test_string = item 
    # using ast.literal_eval() 
    # convert dictionary string to dictionary 
    res = ast.literal_eval(test_string) 
    # print result 
    return res
def to_str(item):
    str1=str(item)
    return str1
def to_arr(item):
    li = list(item.split(" ")) 
    return li 
def list_to_str(item):
    listToStr = ' '.join(map(str, item)) 
    return listToStr



# Create your views here.
def home(request):
    return render(request ,'musicplayer/home.html') 
def song(request):
    v1 =request.GET['search']
    response = requests.get('https://codemusic.vercel.app/search?query='+v1)
    geodata = response.json() 
    print(response)
    return HttpResponse( response, content_type='application/json')
def logout(request):
    auth.logout(request)
    return redirect('/')
def like(request):
    #userid,songid,
    if request.method=='GET':
        if music.objects.filter(user=request.POST['userid']).exists():
            musics=music.objects.get(uid=request.POST['userid'])
            playistcon=playlistCON.objects.get(id=musics.pid)
            songlist=playlistcon.playlistcollection
            k=to_dict(songlist)
            playist=playlist.objects.get(id=k['liked'])
            n=to_arr(playlist.songList)
            if request.POST['songid'] not in n:
                n.append(request.POST['songid'])
                playlist.songList=list_to_str(n)
                playist.save()
        else:
            new=request.POST['songid']
            n=list_to_str(new)
            playist=playlist(songList=n)
            playist.save()
            pid=playist.id
            k={}
            k['liked']=pid
            str1=str(k)
            playlistcon=playlistCON(playlistcollection=str1)
            playlistcon.save()
            x=music(user=request.POST['userid'],pid=playlistcon.id)
            x.save()
        return HttpResponse(response, content_type='application/json')
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
    else:
        response = requests.get('https://codemusic.vercel.app/song?id='+data)
        if response.status_code==200:
            songcred =response.json()
            obj=songs(musicID=songcred['id'], musicTitle=songcred['song'], musicDESC=songcred['primary_artists'],musicIMG=songcred['image'],musicUrl=songcred['media_url'])
            obj.save()
            datas = serializers.serialize('json',songs.objects.all().filter(musicID__exact=data))
            return HttpResponse( datas, content_type='application/json')
    #return render(request,'musicplayer\\songs.html',{'data':geodata})