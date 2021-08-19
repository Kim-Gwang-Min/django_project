from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True) #null처리는 DB에서만 하는 것!
    image = models.ImageField(upload_to='project/', null=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): #이건 장고 모델을 바꿔준게 아니라, 파이썬 안에서의 변화라 migration 안해도 됌
        return f'{self.name}'