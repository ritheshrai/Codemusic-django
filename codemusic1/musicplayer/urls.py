from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.conf.urls import url
urlpatterns = [
    path('', views.home,name='home'),
    path('song',views.song,name='song'),
    path('api',views.api,name='api'),
    path('logout',views.logout,name='logout'),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/musicplayer/image/PePer-ICON.png')),
]