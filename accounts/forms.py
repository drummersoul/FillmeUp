from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
		                'class': 'form-control border-square',
		                'required': 'true',
		                'placeholder': 'Password',
	            	}
            	)
    		)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={
                'class': 'form-control border-square',
                'required': 'true',
                'placeholder': 'First Name',
            	}
                # label='F'
            ),
            "last_name": forms.TextInput(attrs={
                'class': 'form-control border-square',
                'required': 'true',
                'placeholder': 'Last Name',
            	}
                # label='F'
            ),
            "username": forms.TextInput(attrs={
                'class': 'form-control border-square',
                'required': 'true',
                'placeholder': 'Username',
            	}
            ),
            "email": forms.TextInput(attrs={
                'class': 'form-control border-square',
                'required': 'true',
                'placeholder': 'example@example.com',
            	}
            ),
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
	                'class': 'form-control border-square',
	                'required': 'true',
	                'placeholder': 'Username',
            		}
            	)
    		)
    password = forms.CharField(widget=forms.PasswordInput(attrs={
		                'class': 'form-control border-square',
		                'required': 'true',
		                'placeholder': 'Password',
	            	}
	            )
    		)

    class Meta:
        fields = [
            "username",
            "password",
        ]
