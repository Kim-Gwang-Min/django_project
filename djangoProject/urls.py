"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),    #admin은 관리자 페이지 - 장고에서 기본 제공해주는 것, 커스터마이징도 가능!
    path('accounts/', include('accountapp.urls')),    #빨간줄이 뜨면 Alt+enter을 눌러 도움을 받을 수 있음!
    path('profiles/', include('profileapp.urls')),
    path('articles/', include('articleapp.urls')),
    path('comments/', include('commentapp.urls')),
    path('projects/', include('projectapp.urls')),

    path('subscribe/', include('subscribeapp.urls')),
    path('likes/', include('likeapp.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  #이렇게 해줘야 프로필 이미지가 나온다




















