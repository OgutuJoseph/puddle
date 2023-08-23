from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        # # Another Approach
        # widgets = {
        #     'username': forms.TextInput(attrs={
        #         'placeholder': 'Enter Username',
        #         'class': 'w-full py-4 px-6 rounded-xl'
        #     }),
        #     'email': forms.EmailInput(attrs={
        #         'placeholder': 'Enter Email',
        #         'class': 'w-full py-4 px-6 rounded-xl'
        #     })
        # }

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Username',
        'class': 'w-full py-4 px-6 rounded-xl' 
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter Email',
        'class': 'w-full py-4 px-6 rounded-xl' 
    }))
    password1 = forms.CharField(
        # label='Password',
        widget=forms.PasswordInput(attrs={
            'class':'w-full py-4 px-6 rounded-xl', 
            'placeholder':'Enter Password'
        })
    )
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'w-full py-4 px-6 rounded-xl', 
        'placeholder':'Repeat Password'
    }))

# class LoginForm(AuthenticationForm)