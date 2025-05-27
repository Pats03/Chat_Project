# chat_project/urls.py
from django.contrib import admin
from django.urls import path
from chat import views
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('chat/testroom/')),
    path('chat/<str:room_name>/', views.room, name='room'),
]
