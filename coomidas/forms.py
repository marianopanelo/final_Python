from django import forms


class RecetasFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    fecha = forms.DateTimeField(auto_now_add=True)
    ingredientes = forms.TextField()
    preparacion = forms.CharField(max_length=2600) 
    dificultad = forms.IntegerField()
    resumen_de_la_receta = forms.CharField(max_length=200) 
    imagen = forms.ImageField(upload_to='imagenes/', blank=True, null=True)
    username = forms.CharField(max_length=20)

class Comentarios_formulario(forms.Form):
    nombre_receta = forms.CharField(max_length=40)
    nombre_usuario = forms.CharField(max_length=25)
    puntaje = forms.FloatField() 
    comentario = forms.CharField(max_length=450)
    fecha_comentario = forms.DateTimeField(auto_now_add=True)
