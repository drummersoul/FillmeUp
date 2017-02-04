from django import forms

from .models import Volunteer, Review, Report

class VolunteerForm(forms.ModelForm):
	VERIFICATION_CHOICE = (
		(0,"Pending"),
		(1,"Verified"),
	)
	class Meta:
		model = Volunteer
		fields = [
			"name",
			"address",
			"contact_no",
			"website",
			"email",
			"image",
			"content",
			# "verification_status",
		]
		widgets={
			"name":forms.TextInput(attrs={
				'required': 'true',
                'placeholder': 'Name',
                'class': 'form-control',
				}
			),
			"address":forms.TextInput(attrs={
				'required': 'true',
                'placeholder': 'Address',
                'class': 'form-control',
				}
			),
			"contact_no":forms.TextInput(attrs={
				'required': 'true',
                'placeholder': 'Contact No',
                'class': 'form-control',
				}
			),
			"website":forms.TextInput(attrs={
                'placeholder': 'hppts://www.example.com',
                'class': 'form-control',
				}
			),
			"email":forms.TextInput(attrs={
				'required': 'true',
                'placeholder': 'example@example.com',
                'class': 'form-control',
				}
			),
			"registration_no":forms.TextInput(attrs={
				'required': 'true',
                'placeholder': 'Regitration No',
                'class': 'form-control',
				}
			),
			"image":forms.ClearableFileInput(attrs={
				'required': 'true',
				}
			)
		}


class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = [
			"rating",
			"content",
		]
		widgets={
			"rating":forms.Select(attrs={
				'required':'true',
				'class':'form-control'

				}
			),
			"content":forms.Textarea(attrs={
				'required':'true',
				'placeholder':'Review',
				'class':'col-md-10 form-control',
				'rows':'8',
				}
			),
		}

class ReportForm(forms.ModelForm):
	class Meta:
		model = Report
		fields = [
			"title",
			"content",
		]
		widgets={
			"title":forms.TextInput(attrs={
				'required':'true',
				'placeholder':'Title',
				'class':'form-control',
				}
			),
			"content":forms.Textarea(attrs={
				'required': 'true',
                'placeholder': 'Report',
                'class':'col-md-10 form-control',
				'rows':'8',
				}
			),
		}
