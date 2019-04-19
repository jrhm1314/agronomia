from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Publication, Estatus
from ckeditor.fields import RichTextField

class UserCreationFromWithEmail(UserCreationForm):
	email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como maximo y debe ser valido")

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def clean_email(self):
		email = self.cleaned_data.get("email")
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError("El email ya esta registrado, prueba con otro.")

		return email


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['avatar', 'nombre', 'apellido_p', 'apellido_m', 'telefono', 'titulo', 'fecha_nac', 'direccion', 'pais', 'estado', 'ciudad', 'exp', 'edu', 'hab', 'img_exp', 'img_edu', 'img_hab']
		widgets = {
			'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
			'nombre': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':1, 'placeholder':'Nombre'}),
			'apellido_p': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':1, 'placeholder':'Apellido paterno'}),
			'apellido_m': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':1, 'placeholder':'Apellido materno'}),
			'telefono': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':1, 'placeholder':'Telefono'}),
			'titulo': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':1, 'placeholder':'Titulo'}),
			'fecha_nac': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':1, 'placeholder':'fecha de nacimiento (ej. 03/03/2019)'}),
			'direccion': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':1, 'placeholder':'Direccion'}),
			'pais': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':1, 'placeholder':'Pais'}),
			'estado': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':1, 'placeholder':'Estado'}),
			'ciudad': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':1, 'placeholder':'Ciudad'}),
			'exp': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':1, 'placeholder':'Experiencia'}),
			'edu': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':1, 'placeholder':'Educacion'}),
			'hab': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':1, 'placeholder':'Habilidades'}),
			'img_exp': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
			'img_edu': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
			'img_hab': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'})

		}



class PublicationForm(forms.ModelForm):
	class Meta:
		model = Publication
		fields = ['title', 'content','imagen', 'upload', 'estatus']
		widgets = {

			'title': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Titulo'}),
			'content': forms.Textarea(attrs = {'class':'form-control'}),
			'imagen': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
			'upload': forms.ClearableFileInput(attrs = {'class':'form-control-file mt-3'})

		}

		labels = {

			'title':'','content': ''


		}


class EstatusForm(forms.ModelForm):
	class Meta:
		model = Estatus
		fields = ['status']






		


class EmailForm(forms.ModelForm):
	email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como maximo y debe ser valido")
	class Meta:
		model = User
		fields = ['email']

	def clean_email(self):
		email = self.cleaned_data.get("email")
		if 'email' in self.changed_data:
			if User.objects.filter(email=email).exists():
				raise forms.ValidationError("El email ya esta registrado, prueba con otro.")

		return email
