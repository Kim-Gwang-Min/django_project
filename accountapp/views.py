from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()  #HelloWorld() 클래스 가져와서 new 만들기
        new_hello_world.text = temp  #models.py에 temp 넣기
        new_hello_world.save()  #models에 넣었으니 db에 저장

        hello_world_list = HelloWorld.objects.all()  #DB의 모든 데이터를 가져옴


        return render(request, 'accountapp/hello_world.html',
                      context={'hello_world_list': hello_world_list})

    else:
        hello_world_list = HelloWorld.objects.all()   #DB의 모든 데이터를 가져옴

        return render(request, 'accountapp/hello_world.html',
                      context={'hello_world_list': hello_world_list})