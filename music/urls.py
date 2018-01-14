from django.urls import path
from . import views

app_name='music'
urlpatterns = [
    #/music/
    path('', views.index,name='index'),
    #/music/album.id/
    path('<int:album_id>/',views.detail,name='detail'),
    #/music/album.id/favorite/
    path('<int:album_id>/favorite/',views.favorite,name='favorite'),
]