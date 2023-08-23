from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    password1 = forms.CharField(
        # label='Password',
        widget=forms.PasswordInput(attrs={'class':'w-full py-4 px-6 rounded-xl', 'type':'password', 'placeholder':'Enter Password'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'w-full py-4 px-6 rounded-xl', 'type':'password', 'placeholder':'Repeat Password'})
    )

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
            # !!NOT WORKING -- USE Above ^^ Implementation
            # 'password1': forms.PasswordInput(attrs={
            #     'placeholder': 'Enter Email',
            #     'class': 'w-full py-4 px-6 rounded-xl'
            # }),
            # 'password2': forms.PasswordInput(attrs={
            #     'placeholder': 'Repeat Password',
            #     'class': 'w-full py-4 px-6 rounded-xl'
            # })
        }

        # !!NOT WORKING!!
        # username = forms.CharField(widget=forms.TextInput(attrs={
        #     'placeholder': 'Enter Username',
        #      'class': 'w-full py-4 px-6 rounded-xl'           
        # }))