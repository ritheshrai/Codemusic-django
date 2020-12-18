from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.conf.urls import url
urlpatterns = [
    path('', views.index,name='index'),
    path('/register',views.register,name='register'),
    path('/signin',views.signin,name='signin'),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/musicplayer/image/PePer-ICON.png')),
]