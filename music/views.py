from django.shortcuts import render,get_object_or_404
from .models import Album
def index(request):
    allAlbum=Album.objects.all()
    return render(request,'music/index.html',{'allAlbum':allAlbum})

def detail(request,album_id):
    album=get_object_or_404(Album, pk=album_id)
    return render(request, 'music/details.html', {'allAlbum': album})

def favorite(request,album_id):
    album=get_object_or_404(Album,pk=album_id)
    try:
        selected_song=album.song_set.get(pk=request.POST['song'])
    except (KeyError,Song.DoesNotExist):
        return render(request,'music/details.html',{
    'allAlbum':allAlbum,
    'error_message' : "You didnot select a valid song",
    })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request,'music/details.html',{'allAlbum':album})