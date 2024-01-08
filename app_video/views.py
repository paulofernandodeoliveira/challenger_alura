from django.shortcuts import render, get_object_or_404
from .models import Video

def home(request):
    videos = Video.objects.all()
    return render(request, 'todos_os_videos/todos_os_videos.html', {'videos': videos})



def video_especifico(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    return render(request, 'todos_os_videos/videos_unico.html', {'video': video})

def cadastrar_videos(request):
    return render (request, 'todos_os_videos/cadastrar_videos.html')