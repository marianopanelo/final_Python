from django.contrib import admin
from django.urls import path
from coomidas import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio,name = 'inicio' ),
    path('registro/', views.agregar_usuario,name = 'agregar_usuario'),
    path('login/', views.login_usuario , name = 'login'),
    path('nosotros/', views.nosotros , name = 'nosotros'),
    path('perfil/', views.perfil , name = 'perfil'),
    path('perfil_rellenar/', views.terminar_de_rellenar_perfil, name = 'Terminar_de_rellenar_perfil'),
    path('edit/', views.editar_perfil , name="editar_perfil"),
    path('edit_nombre_apellido/', views.editar_nombre_apellido, name="editar_nombre_apellido"),
    path('eliminar_perfil/', views.eliminar_perfil, name="eliminar_perfil"),
    path('logout/', LogoutView.as_view(template_name='index.html'), name="logout"),


    path('recetas', views.RecetasVistas.as_view(), name = 'recetas_vistas'),
    path('recetas/detalle/<int:pk>/', views.PostreDetalle.as_view(), name = 'Detalle_receta'),
    path('recetas/crear/', views.RecetasCreate.as_view(), name = 'recetas_crear'),
    path('recetas/editar/<int:pk>/', views.RecetasUpdate.as_view(), name = 'recetas_modificar'),
    path('recetas/eliminar/<int:pk>/', views.RecetasDelete.as_view(), name = 'recetas_eliminar'),

    path('comentario/crear/<int:receta_id>/', views.ComentarioCreate.as_view(), name = 'comentario_crear'),
    path('comentarios/', views.ComentariosVistas.as_view(), name = 'vista_comentarios'),
    path('comentarios/editar/<int:pk>/', views.ComentariosUpdate.as_view(), name = 'editar_comentario'),
    path('comentarios/eliminar/<int:pk>/', views.ComentariosDelete.as_view(), name = 'eliminar_comentario'),

    path('<path:catchall>/', views.error),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

