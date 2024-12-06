from django import forms
from myapp.models.user import User

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nome', 'senha']

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nome', 'senha', 'email','cpf']


