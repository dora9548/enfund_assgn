from django.shortcuts import render
from .models import Chat
from django.contrib.auth.models import User


def load_chat(request, room_name):
    messages = Chat.objects.filter(
        sender=request.user, receiver__username=room_name
    ) | Chat.objects.filter(
        sender__username=room_name, receiver=request.user
    )
    return render(request, 'chat/chat_room.html', {'messages': messages})


def chat_room(request):
    users = User.objects.exclude(username=request.user.username)  # Exclude current user
    return render(request, 'chat/chat_room.html', {'users': users})