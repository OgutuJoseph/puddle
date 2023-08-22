from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Enter Username',
                'class': 'w-full py-4 px-6 rounded-xl'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter Email',
                'class': 'w-full py-4 px-6 rounded-xl'
            }),
            'password1': forms.TextInput(attrs={
                'placeholder': 'Enter Password',
                'class': 'w-full py-4 px-6 rounded-xl'
            }),
            'password2': forms.PasswordInput(attrs={
                'placeholder': 'Repeat Password',
                'class': 'w-full py-4 px-6 rounded-xl'
            })
        }

        # !!NOT WORKING!!
        # username = forms.CharField(widget=forms.TextInput(attrs={
        #     'placeholder': 'Enter Username',
        #      'class': 'w-full py-4 px-6 rounded-xl'           
        # }))