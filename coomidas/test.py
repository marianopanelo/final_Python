from django.test import TestCase, Client
from django.urls import reverse
from coomidas.models import Usuario_perfil,Recetas,Comentarios
from django.contrib.auth.models import User
from datetime import datetime


class ComentariosUpdateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = Client()
        self.client.login(username='testuser', password='12345')

        self.comentario = Comentarios.objects.create(
            nombre_usuario="prueba",
            nombre_receta="prueba",
            puntaje=5,
            comentario="prueba",
            fecha_comentario=datetime.now()
        )
        
        self.url = reverse("editar_comentario", args=[self.comentario.id])

    def test_update_comentario(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "comentarios/editar_comentario.html")

        response = self.client.post(self.url, {
            'puntaje': 8,
            'comentario': 'comentario actualizado',
        })
        
        self.comentario.refresh_from_db()  
        self.assertEqual(self.comentario.puntaje, 8)
       
        self.assertRedirects(response, reverse('vista_comentarios'))



class RecetaUpdateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = Client()
        self.client.login(username='testuser', password='12345')
        self.receta = Recetas.objects.create(
            nombre="prueba",
            ingredientes="prueba",
            preparacion="prueba",
            dificultad=5,
            resumen_de_la_receta="prueba"
        )
        self.url = reverse("recetas_modificar", args=[self.receta.id])
    
    def test_update_receta(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recetas/editar_recetas.html")
        response = self.client.post(self.url, {
            'dificultad': 1,
            'nombre': self.receta.nombre,  
            'ingredientes': self.receta.ingredientes,
            'preparacion': self.receta.preparacion,
            'resumen_de_la_receta': self.receta.resumen_de_la_receta
        })
        
        self.receta.refresh_from_db()       
        self.assertEqual(self.receta.dificultad, 1)
        self.assertRedirects(response, reverse('recetas_vistas'))



class EliminarComentarios(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = Client()
        self.client.login(username='testuser', password='12345')
        self.receta = Comentarios.objects.create(
            nombre_usuario="prueba",
            nombre_receta="prueba",
            puntaje=5,
            comentario="prueba",
            fecha_comentario=datetime.now()
        )
        self.url = reverse("eliminar_comentario", args=[self.receta.id])
    
    def test_eliminar_receta(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, "comentarios/eliminar_comentario.html")
        response = self.client.post(self.url)        
        self.assertEqual(Comentarios.objects.count(), 0)       
        self.assertRedirects(response, reverse('vista_comentarios'))


class EliminarReceta(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = Client()
        self.client.login(username='testuser', password='12345')
        self.receta = Recetas.objects.create(
            nombre="prueba",
            ingredientes="prueba",
            preparacion="prueba",
            dificultad=5,
            resumen_de_la_receta="prueba"
        )
        self.receta.nombre = "pepe"
        self.receta.save()
        self.url = reverse("recetas_eliminar", args=[self.receta.id])
    
    def test_eliminar_receta(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, "recetas/eliminar_receta.html")
        response = self.client.post(self.url)        
        self.assertEqual(Recetas.objects.count(), 0)       
        self.assertRedirects(response, reverse('inicio'))




"""
class EliminarUsuario(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = Client()
        self.client.login(username='testuser', password='12345')
        self.usuario = Usuario_perfil.objects.create(
            nombre="prueba",
            apellido="prueba",
            username="prueba"
        )
        self.url = reverse("eliminar_perfil", args=[self.usuario.id])
    
    def test_eliminar_usuario(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, "usuarios/eliminar_perfil.html")
        response = self.client.post(self.url)        
        self.assertEqual(Usuario_perfil.objects.count(), 0)       
        self.assertRedirects(response, reverse('inicio'))
"""


        

