from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import  HttpResponse, JsonResponse
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def room(request, pk):
    username = request.GET.get('username')
    room_id = Room.objects.get(name=pk)

    return render(request, 'room.html', {
        'roomname':pk,
        'username': username,
        'room_id': room_id.id,
        })

def checkdata(request):
    roomname = request.POST['roomname']
    username = request.POST['username']  

    if Room.objects.filter(name=roomname).exists():
        return redirect('room/'+roomname+'/?username='+username)
    else:
        messages.info(request, 'Invalid room name please click on create room to create one')
        return redirect("/")

def send(request):
    message = request.POST['message']
    room_id = request.POST['room_id']
    username = request.POST['username']

    new_message = Message.objects.create(value=message, user= username, room=room_id)
    new_message.save()
    return HttpResponse('message send done')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)

    return JsonResponse({
        'messages': list(messages.values())
    })

def create_room(request):
    new_roomname = request.POST['newroomname']

    if Room.objects.filter(name=new_roomname).exists():
        return JsonResponse({'messages': 'This room name is already exists please try another one'})
    else:
        new_room = Room.objects.create(name=new_roomname)
        new_room.save()
        return JsonResponse({'messages': 'Room created successfully'})

