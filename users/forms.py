from django import forms
from .models import UserProfile
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = [
			"contact_no",
			"image",
			"bio",
			"birth_date",
			"address",
			"country",
		]
		widgets={
			"contact_no":forms.TextInput(attrs={
				'required':'true',
				'placeholder':'Contact No',
				'class': 'form-control',
				}
			),
			"image":forms.ClearableFileInput(attrs={
				'required':'true',
				'placeholder':'Image',
				}
			),

			"bio":forms.Textarea(attrs={
				'required':'true',
				'placeholder':'Bio',
				'class': 'form-control col-md-10',
				'rows':'8',
				}
			),
			"birth_date":forms.DateInput(attrs={
				'required':'true',
				'placeholder':'Birthdate',
				'class': 'form-control',
				}
			),
			"address":forms.TextInput(attrs={
				'required': 'true',
                'placeholder': 'Address',
                'class': 'form-control',
				}
			),
			"country":forms.TextInput(attrs={
				'required': 'true',
                'placeholder': 'Country',
                'class': 'form-control',
				}
			),
			
		}

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [
			"first_name",
			"last_name",
			"email",
		]
		widgets = {
            "first_name": forms.TextInput(attrs={
                'required': 'true',
                'placeholder': 'First Name',
                'class': 'form-control',
            	}
                # label='F'
            ),
            "last_name": forms.TextInput(attrs={
                'required': 'true',
                'placeholder': 'Last Name',
                'class': 'form-control',
            	}
                # label='F'
            ),
            "email": forms.TextInput(attrs={
                'required': 'true',
                'placeholder': 'example@example.com',
                'class': 'form-control',
            	}
            ),
        }
