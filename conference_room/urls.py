"""conference_room URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from room_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name='home'),
    path('rooms', views.RoomView.as_view(), name='Rooms'),
    path('room/new', views.RoomAdd.as_view(), name='newRoom'),
    path('room/<int:id>', views.RoomDetails.as_view(), name='RoomDetails'),
    path('room/modify/<int:id>', views.RoomModify.as_view(), name='RoomModify'),
    path('room/delete/<int:id>', views.RoomDelete.as_view(), name='RoomDelete'),
    path('room/reserve/<int:id>', views.RoomReserve.as_view(), name='RoomReserve'),
]
