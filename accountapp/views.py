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

        return render(request, 'accountapp/hello_world.html',
                      context={'hello_world_output': new_hello_world})
    else:
        return render(request, 'accountapp/hello_world.html',
                      context={'text': 'GET METHOD!'})