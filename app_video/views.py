from django.shortcuts import render
from .models import Video

def home(request):
    videos = Video.objects.all()
    return render(request, 'todos_os_videos/todos_os_videos.html', {'videos': videos})