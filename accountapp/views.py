from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()  #HelloWorld() 클래스 가져와서 new 만들기
        new_hello_world.text = temp  #models.py에 temp 넣기
        new_hello_world.save()  #models에 넣었으니 db에 저장

        return HttpResponseRedirect(reverse('accountapp:hello_world'))    #accountapp안에 hello_world 라우터에 재연결 해라! 그래야 Post 요청을 계속 반복 안함!

    else:
        hello_world_list = HelloWorld.objects.all()   #DB의 모든 데이터를 가져옴
        hello_world_list.delete()
        return render(request, 'accountapp/hello_world.html',
                      context={'hello_world_list': hello_world_list})




class AccountCreateView(CreateView):   #AccountCreateView라는 이름의 class를 만들 건데, CreatView를 상송받아라!
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')  #reverse와 무슨 차이냐면, class 안에서는 reverse_lazy를 해야함!
    template_name = 'accountapp/create.html'  #create.html 라우터를 만듬