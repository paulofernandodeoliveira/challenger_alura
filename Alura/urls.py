from django.contrib import admin
from django.urls import path, include, re_path
from app_video import views
urlpatterns = [
    # Exemplos:
    # path('', Alura.views.home, name='home'),
    # path('blog/', include('blog.urls')),
    path('videos', views.home, name='home'),
]
