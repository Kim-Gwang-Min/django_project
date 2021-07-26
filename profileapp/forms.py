from django.forms import ModelForm
from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']
        #클라이언트로부터 이 3가지를 받을 것이라고 명시! 모델에 작성한 4가지 중 3가지!
        #user는 DB에서 처리할 것임!