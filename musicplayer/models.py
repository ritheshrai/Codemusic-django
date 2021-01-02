from django.db import models
from django.conf import settings
# Create your models here.
class music(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pid=models.ForeignKey('playlistCON',on_delete=models.CASCADE)     
class songs(models.Model):
    musicID = models.CharField(max_length=50)
    musicTitle = models.CharField(max_length=100)
    musicDESC = models.TextField()
    musicIMG = models.URLField(max_length=200)
    musicUrl = models.URLField(max_length=200)
    fame=models.DecimalField(db_index=True,max_digits=5, decimal_places=2,default=0)
class  playlistCON (models.Model):
    playlistcollection = models.TextField()
class playlist(models.Model):
    songList=models.TextField()  
  
