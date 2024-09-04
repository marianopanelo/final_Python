from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User    
from coomidas.models import Usuario_perfil

class Crear_usuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_text = {k: "" for k in fields}

class editar_usuario(UserChangeForm):
    
    password = None
    email = forms.EmailField(label="ingrese su mail")
    username =  forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ["email", "username"]
        help_text = {k: "" for k in fields}


class Final_formulario_perfil(forms.Form):
    nombre = forms.CharField(max_length=20) 
    apellido = forms.CharField(max_length=20) 
    username = forms.CharField(max_length=20)


class editar_formulario_perfil(forms.ModelForm):
    class Meta:
        model = Usuario_perfil
        fields = ['nombre', 'apellido']


class editar_userName(forms.ModelForm):
    class Meta:
        model = Usuario_perfil
        fields = ['username']


