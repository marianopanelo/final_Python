# Proyecto Django - Mi Aplicación de Recetas

## Descripción

Este proyecto es una aplicación web para gestionar recetas y comentarios de recetas. Permite a los usuarios crear, editar, eliminar recetas y comentarios, así como ver detalles de recetas específicas.

## Instalación

1. **Clonar el Repositorio**

   Clona el repositorio en tu máquina local:

   ```bash
   git clone <URL_DEL_REPOSITORIO>

Crear y Activar un Entorno Virtual

python -m venv entorno-virtual
source entorno-virtual/bin/activate

Instalar Dependencias
pip install -r requirements.txt

Migrar la Base de Datos
python manage.py migrate

Cargar Datos Iniciales (opcional)
python manage.py loaddata <nombre_del_archivo>.json

Iniciar el Servidor de Desarrollo
python manage.py runserver

Uso
Páginas Principales
Inicio: http://127.0.0.1:8000/ - Página de inicio.
Registro: http://127.0.0.1:8000/registro/ - Registro de nuevos usuarios.
Login: http://127.0.0.1:8000/login/ - Ingreso de usuarios existentes.
Perfil: http://127.0.0.1:8000/perfil/ - Ver y editar el perfil del usuario.
Recetas: http://127.0.0.1:8000/recetas/ - Ver lista de recetas.
Crear Receta: http://127.0.0.1:8000/recetas/crear/ - Crear una nueva receta.
Detalles de Receta: http://127.0.0.1:8000/recetas/detalle/<id>/ - Ver detalles de una receta específica.
Comentarios: http://127.0.0.1:8000/comentarios/ - Ver lista de comentarios.
Rutas
/recetas/crear/: Página para crear una nueva receta.
/recetas/editar/int:pk/: Página para editar una receta existente.
/recetas/eliminar/int:pk/: Página para eliminar una receta.
/comentario/crear/int:receta_id/: Página para crear un comentario para una receta.
/comentarios/editar/int:pk/: Página para editar un comentario existente.
/comentarios/eliminar/int:pk/: Página para eliminar un comentario.
Manejo de Errores
Página no encontrada: La aplicación redirige a una página de error si se accede a una URL no definida.






super usuario
usuario = mariano
contraseña = Finalcoder


