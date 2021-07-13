from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accountapp.views import hello_world, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('login/', LoginView.as_view(template_name='accountapp/Login.html'), name='login'),
    #로직은 장고가 만들어둔 loginview를 가져오면 된다!, 그리고 아이디 비번 입력할 페이지만 만들면 된다! 이건 login.html로~ #

    path('logout/', LogoutView.as_view(), name='logout'),
    #장고가 만들어둔 logoutview를 가져오자!#

    path('create/', AccountCreateView.as_view(), name='create')
    # 회원가입 페이지 연결 #
]
