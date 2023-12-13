from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class ChangeUserData(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email']
