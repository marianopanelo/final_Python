from django.db import models
import json
import os #es para las imagenes


class Usuario_perfil(models.Model):
    nombre = models.CharField(max_length=20) 
    apellido = models.CharField(max_length=20) 
    username = models.CharField(max_length=20)


class Recetas(models.Model):
    nombre = models.CharField(max_length=40)
    fecha = models.DateTimeField(auto_now_add=True)
    ingredientes = models.TextField()
    preparacion = models.CharField(max_length=2600) 
    dificultad = models.IntegerField()
    resumen_de_la_receta = models.CharField(max_length=1000)
    username = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)

    #para ingresar los ingredientes, igual que antes
    def agregar_ingrediente(self, ingrediente):
        ingredientes = self.get_ingredientes()
        ingredientes.append(ingrediente)
        self.ingredientes = json.dumps(ingredientes)
        self.save()

    #para eliminar la imagen
    def delete(self, *args, **kwargs):
        if self.imagen:
            if os.path.isfile(self.imagen.path):
                os.remove(self.imagen.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.nombre

class Comentarios(models.Model):
    nombre_usuario = models.CharField(max_length=25)
    nombre_receta = models.CharField(max_length=40)
    puntaje = models.FloatField() 
    comentario = models.CharField(max_length=450)
    fecha_comentario = models.DateTimeField(auto_now_add=True)