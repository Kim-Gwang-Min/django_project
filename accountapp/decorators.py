from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    #데코레이터 이름을 account_ownership_required로 하자!
    def decorated(request, *args, **kwargs):
        #꾸밈을 받을 내부 함수도 선언해주자! 그 함수가 받는 인자는 3가지다.
        target_user = User.objects.get(pk=kwargs['pk'])
        #db에 접근해서 target_user를 가져와서 requst_user와 비교해야한다.
        #User.objects.all을 hello_world 로직에서 작성해봤다~
        #이번에는 all이 아니라 get만 할건데, pk값을 받아서 특정 user만 가져올가다.
        if target_user == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return decorated
    #decorated() 이렇게 작성하면 함수를 호출하는게 된다.. 그런데 데코레잍는 함수를 그대로 return하는 거다.
