from django.shortcuts import render 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login , authenticate
from coomidas.forms_usuario import Crear_usuario , editar_usuario,Final_formulario_perfil,editar_formulario_perfil
from coomidas.models import Recetas , Usuario_perfil ,Comentarios
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def inicio(request):
    return render(request, 'index.html', {"user": request.user})


def agregar_usuario(request):
    
    msg_register = ""
    if request.method == 'POST':

        form = Crear_usuario(request.POST)
        if form.is_valid():
            form.save()
                        
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password1')
            user = authenticate(username=usuario, password=contrasenia)
            login(request, user)

            return render(request, "usuarios/perfil_usuario.html",{"user": user})
            
        msg_register = "Error en los datos ingresados"

    form = Crear_usuario()     
    return render(request,"usuarios/agregar_usuario.html" ,  {"form":form, "msg_register": msg_register})


def login_usuario(request):
    msg_login = ""
    if request.method == 'POST': 
        form = AuthenticationForm(request, data=request.POST) 

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia) 

            if user is not None: 
                login(request, user)
                usuario = Usuario_perfil.objects.filter(username=request.user.username).first()
                return render(request, "usuarios/perfil_usuario.html",{"user": user, "datos_finales_usuario":usuario})

        msg_login = "Usuario o contraseña incorrectos" 

    form = AuthenticationForm()
    return render(request, "usuarios/loguin.html", {"form": form, "msg_login": msg_login})


@login_required
def perfil(request):
    
    usuario = Usuario_perfil.objects.filter(username=request.user.username).first()
    return render(request , 'usuarios/perfil_usuario.html', {"datos_finales_usuario": usuario})


@login_required
def terminar_de_rellenar_perfil(req):
    """
    Vista para crear nuevas recetas a través de un formulario.
    """
    if req.method == 'POST' : 
        miFormulario = Final_formulario_perfil(req.POST) 


        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            datos_finales_usuario = Usuario_perfil(nombre=info['nombre'], apellido=info['apellido'], username=info['username'])
            datos_finales_usuario.save()
            
            return render (req, "usuarios/perfil_usuario.html",{"datos_finales_usuario": datos_finales_usuario})
    else: 
        miFormulario = Final_formulario_perfil()

    return render(req , 'usuarios/rellenar_perfil.html',{"formulario": miFormulario})


@login_required
def editar_perfil(request):
    """
    Función de vista para manejar la edición del perfil de usuario.
    """
    usuario = request.user  
    username_viejo = usuario.username
    if request.method == 'POST':  # Verificar si la solicitud es un POST (envío de formulario)

        miFormulario = editar_usuario(request.POST, request.FILES, instance=usuario) 
        miFormulario.save()  
        if Usuario_perfil.objects.filter(username=username_viejo):
            perfil = Usuario_perfil.objects.get(username=username_viejo)
            perfil.username = request.POST.get('username')
            perfil.save()
            return render(request, 'index.html')   
        else:
            return render(request, 'index.html')

    else:  
        
        miFormulario = editar_usuario(instance=usuario) 

    # Renderizar la plantilla 'editar_usuario.html', pasando el formulario y los datos del usuario
    return render(request, "usuarios/editar_usuario.html", {"mi_form": miFormulario, "usuario": usuario})


@login_required
def editar_nombre_apellido(request):
    perfil = Usuario_perfil.objects.get(username=request.user.username)
    
    if request.method == 'POST':
        form = editar_formulario_perfil(request.POST, instance=perfil)
        
        if form.is_valid():
            form.save()
            return render(request, 'index.html')  
    else:
        form = editar_formulario_perfil(instance=perfil)

    return render(request, 'usuarios/editar_nombre_apellido.html', {'form': form})


@login_required
def eliminar_perfil(request):
    if request.method == 'POST':
        usuario = request.user
        perfil2 = User.objects.get(username=usuario)
        perfil2.delete()
        if Usuario_perfil.objects.get(username=usuario) :
            perfil = Usuario_perfil.objects.get(username=usuario)
            perfil.delete()
            return render(request,'index.html')
        return render(request,'index.html')
    return render(request,'usuarios/usuario_eliminar.html')


def nosotros(req):
    return render(req , 'nosotros.html')


class RecetasVistas(LoginRequiredMixin ,ListView):
    """
    Vista para mostrar las recetas
    """
    model = Recetas
    template_name = "recetas/recetas.html"


class PostreDetalle(LoginRequiredMixin , DetailView):
    """
    Vista para mostrar los detalles de un postre específico.
    """
    model = Recetas
    template_name = "recetas/receta_grende.html"


class RecetasCreate(LoginRequiredMixin ,CreateView):
    """
    Vista para crear nuevas recetas a través de un formulario.
    """
    model = Recetas
    template_name = "recetas/agregar_recetas.html"
    success_url = reverse_lazy("recetas_vistas") 
    fields = ["nombre","ingredientes","preparacion","dificultad","resumen_de_la_receta","imagen","username"]

    def form_valid(self, form):

        ingredientes = form.cleaned_data.get('ingredientes')
        
        
        ingredientes_list = [ing.strip() for ing in ingredientes.split('\r') if ing.strip()] 
        print(ingredientes_list)
        
        ingredientes_con_saltos = '\n'.join(ingredientes_list)
        print(ingredientes_con_saltos)

        form.instance.ingredientes = ingredientes_con_saltos

        return super().form_valid(form)


class RecetasUpdate(LoginRequiredMixin ,UpdateView):
    """
    Vista para editar vistas existentes a través de un formulario
    """
    model = Recetas
    template_name = "recetas/editar_recetas.html"
    success_url = reverse_lazy("recetas_vistas")
    fields = ["nombre", "ingredientes", "preparacion", "dificultad", "resumen_de_la_receta", "imagen"]


class RecetasDelete(LoginRequiredMixin ,DeleteView):
    """
    Vista para eliminar recetas.
    """
    model = Recetas
    success_url = reverse_lazy("inicio")  
    template_name = "recetas/eliminar_receta.html"  


class ComentarioCreate(LoginRequiredMixin ,CreateView):
    """
    Vista para crear nuevas recetas a través de un formulario.
    """
    model = Comentarios
    template_name = "comentarios/comentar_receta.html"
    success_url = reverse_lazy("vista_comentarios") 
    fields = ["nombre_receta","nombre_usuario","comentario","puntaje"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        receta_id = self.kwargs.get('receta_id')  
        receta = Recetas.objects.get(id=receta_id)  
        context['receta'] = receta  
        return context


class ComentariosVistas(LoginRequiredMixin ,ListView):
    """
    Vista para mostrar las recetas
    """
    model = Comentarios
    context_object_name = "comentarios"
    template_name = "comentarios/vista_comentarios.html"

class ComentariosUpdate(LoginRequiredMixin ,UpdateView):
    """
    Vista para editar vistas existentes a través de un formulario
    """
    model = Comentarios
    template_name = "comentarios/editar_comentario.html"
    success_url = reverse_lazy("vista_comentarios")
    fields = ["puntaje", "comentario"]


class ComentariosDelete(LoginRequiredMixin ,DeleteView):
    """
    Vista para eliminar recetas.
    """
    model = Comentarios
    success_url = reverse_lazy("vista_comentarios")  
    template_name = "comentarios/eliminar_comentario.html"  


def error(request, *args, **kwargs):
    return render(request, 'error.html', status=404)