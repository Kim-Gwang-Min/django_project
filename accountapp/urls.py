from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('login/', LoginView.as_view(template_name='accountapp/Login.html'), name='login'),
    #로직은 장고가 만들어둔 loginview를 가져오면 된다!, 그리고 아이디 비번 입력할 페이지만 만들면 된다! 이건 login.html로~ #

    path('logout/', LogoutView.as_view(), name='logout'),
    #장고가 만들어둔 logoutview를 가져오자!#

    path('create/', AccountCreateView.as_view(), name='create'),
    # 회원가입 페이지 연결 #

    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    # 계정 상세페이지 연결 #

    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    # 계정정보 수정 페이지 연결 #

    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete')
    # 계정 탈퇴 페이지 연결 #
]












