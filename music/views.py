from django.http import HttpResponse
# from django.template import loader
# from django.shortcuts import render,get_object_or_404
# from .models import Album, Song
#
#
# def index(request):
#     all_albums=Album.objects.all()
#     # template=loader.get_template('music/index.html')
#     context={
#         'all_albums':all_albums
#     }
#
#     return render(request,'music/index.html',context)
#
# # def index(request):
# #     all_albums=Album.objects.all()
# #     html=''
# #     for album in all_albums:
# #         url= '/music/'+str(album.id)+'/'
# #         html+='<a href="' + url+'">'+album.album_title+'</a><br>'
# #     return HttpResponse(html)
#
# def detail(request,album_id):
#     album=get_object_or_404(Album,pk=album_id)
#
#     return render(request,'music/deteils.html',{'album':album})
#
# def favorite(request,album_id):
#     album=get_object_or_404(Album,pk=album_id)
#     try:
#         selctec_song=album.song_set.get(pk=request.POST['song'])
#     except(KeyError, Song.DoesNotExist):
#         return render(request, 'music/deteils.html', {'album': album,
#                                                       'error_massage':"ahangi entekhab nakardi",
#                                                       })
#     else:
#         selctec_song.is_favorite=True
#         selctec_song.save()
#     return render(request, 'music/deteils.html', {'album': album})
#
#
#
from django.views import generic
from .models import Album


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'
    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/deteils.html'






















