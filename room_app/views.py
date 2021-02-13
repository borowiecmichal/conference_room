from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from room_app.models import Room

class Home(View):
    def get(self, request):
        return render(request, 'confeence_room.html')

class RoomView(View):
    def get(self, request):
        r = Room.objects.all()
        return render(request, 'roomView.html', {'rooms':r})
class RoomAdd(View):
    def get(self, request):
        return render(request, 'addRoom.html')