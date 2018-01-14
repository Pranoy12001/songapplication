from django.shortcuts import render,get_object_or_404
from .models import Album
def index(request):
    allAlbum=Album.objects.all()
    return render(request,'music/index.html',{'allAlbum':allAlbum})

def detail(request,album_id):
    album=get_object_or_404(Album, pk=album_id)
    return render(request, 'music/details.html', {'allAlbum': album})
