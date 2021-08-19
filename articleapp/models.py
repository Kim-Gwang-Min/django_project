from django.contrib.auth.models import User
from django.db import models
from projectapp.models import Project


class Article(models.Model):  #게시글에 필요한 것들을 작성해보자~
    writer = models.ForeignKey(User,
                               on_delete=models.SET_NULL,
                               related_name='article',
                               null=True)  #User와의 연결고리
    project = models.ForeignKey(Project,
                                on_delete=models.SET_NULL, #게시판이 삭제되어도 게시글은 남아있음
                                related_name='article',
                                null=True)   #Project와의 연결고리
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=True)
    content = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
#프로필앱에서는 onetoone으로 1:1 매칭해야하지만,
#게시글은 한 유저가 여러가지 게시글을 작성할 수 있으므로,
#ForeignKey로 연결만 해주면 된다~

# 모델이 변화하면 migration, migrate해야한다!