from django.views import generic
from .models import Album, Song

class IndexView(generic.ListView):
    template_name='music/index.html'
    context_object_name="all_album"
    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model=Album
    template_name='music/details.html'
    context_object_name="all_album"
    def get_queryset(self):
        return Album.objects.all()