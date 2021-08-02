from django.http import HttpResponseForbidden
from profileapp.models import Profile


def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_profile = Profile.objects.get(pk=kwargs['pk'])  #DB에서 유저를 가져오자.
        if target_profile.user == request.user:  #프로필 유저가 요청보내는 유저랑 같은지 비교
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return decorated

