from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #super()은 부모클래스의 메서드에 적급할 때 쓰는 메서드

        self.fields['username'].disabled = True
        #username이라는 fields를 찾아서 비활성화 하자!