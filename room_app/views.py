from datetime import datetime

from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

import room_app
from room_app.models import Room, Reservation


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
        return render(request, 'editRoom.html', {'room': room})

    def post(self, request, id):
        room = Room.objects.get(pk=id)

        try:
            room_by_name = Room.objects.get(name=request.POST['name'])
            if room_by_name.id == room.id:
                name_availability = True
            else:
                name_availability = False
        except room_app.models.Room.DoesNotExist:
            name_availability = True

        if request.POST['name'] and name_availability:
            try:
                capacity = int(request.POST['capacity'])
                if capacity >= 0:
                    room.name = request.POST['name']
                    room.capacity = request.POST['capacity']
                    proj = request.POST.get('projector', None)
                    if proj == 'available':
                        room.projector_availability = True
                    else:
                        room.projector_availability = False
                    room.save()
                else:
                    return render(request, 'editRoom.html', {'room': room, 'error': 'Wrong input data'})
            except ValueError:
                return render(request, 'editRoom.html', {'room': room, 'error': 'Wrong input data'})
        else:
            return render(request, 'editRoom.html', {'room': room, 'error': 'Wrong room name, try again'})

        return redirect('Rooms')


class RoomReserve(View):
    def get(self, request, id):
        room = Room.objects.get(pk=id)
        return render(request, 'roomReserve.html', {'room': room})

    def post(self, request, id):
        room = Room.objects.get(pk=id)

        date = request.POST['date']
        datetime_object = datetime.strptime(date, '%Y-%m-%d').date()
        # a=list(room.reservation_set.all())
        a=[]
        for elem in room.reservation_set.all():
            a.append(elem.date)

        if datetime_object in a or datetime_object < datetime.now().date():
            return render(request, 'roomReserve.html', {'error': 'This date is unavailable'})

        else:
            Reservation.objects.create(comment=request.POST['comment'], date=datetime_object, room=room)
        return redirect('Rooms')


class RoomDetails(View):
    pass
