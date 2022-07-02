from django.shortcuts import render
import datetime

# Create your views here.


def home(request):
    return render(request, 'connectapp/home.html')


def game(request, room_name):
    id = request.session['identifier'] = datetime.datetime.now().timestamp()
    print("4k:  "+str(id))
    return render(request, 'connectapp/index.html', {
        'room_name': room_name, 'id':id
    })
