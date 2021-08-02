from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):  #장고가 기본제공하는 model상속받기
    user = models.OneToOneField(User, on_delete=models.CASCADE,     #1:1계정 연결, OneToOneField로 1:1 연결, User import,
                                related_name='profile')  #관련된 이름 : user객체에서 profile객체에 접근하고 싶을 때 연결 name 예) target_user.profile

    image = models.ImageField(upload_to='profile/', null=True)   #settings에서 이미지를 받는다고 해줬는데 그 안에서 어디에? uplode_to는 어떤 경로에 이미지를 저장할 것인지 작성!
    nickname = models.CharField(max_length=30, unique=True, null=True) #회원들간에 닉네임이 겹치지 않게 유니크하게
    message = models.CharField(max_length=200, null=True ) #대화명, 상태메세지, null값을 true로 해주면 메세지가 없어도 괜찮아진다!







