from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

import room_app
from room_app.models import Room


class Home(View):
    def get(self, request):
        return render(request, 'confeence_room.html')


class RoomView(View):
    def get(self, request):
        r = Room.objects.all()
        return render(request, 'roomView.html', {'Rooms': r})


class RoomAdd(View):
    def get(self, request):
        return render(request, 'addRoom.html')

    def post(self, request):
        name = request.POST['name']
        capacity = request.POST['capacity']
        proj = request.POST.get('projector', None)
        if proj == 'available':
            proj_availability = True
        else:
            proj_availability = False

        try:
            room_check = Room.objects.get(name=name)
            name_availability = False
        except room_app.models.Room.DoesNotExist:
            name_availability = True

        if name and name_availability:
            try:
                capacity = int(capacity)
                if capacity >= 0:
                    Room.objects.create(name=name, capacity=capacity, projector_availability=proj_availability)
                else:
                    return render(request, 'addRoom.html', {'error': 'Wrong input data'})
            except ValueError:
                return render(request, 'addRoom.html', {'error': 'Wrong input data'})
        else:
            return render(request, 'addRoom.html', {'error': 'Wrong room name, try again'})

        return redirect('home')


class RoomDelete(View):
    def get(self, request, id):
        room = Room.objects.get(pk=id)
        room.delete()
        r = Room.objects.all()
        return render(request, 'roomView.html', {'Rooms': r})
        return render(request, 'roomView.html')


class RoomModify(View):
    def get(self, request, id):
        room = Room.objects.get(pk=id)
        return render(request, 'editRoom.html', {'room':room})


class RoomDetails(View):
    pass
