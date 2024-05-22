from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import estudiante
from .forms import estudianteForm

# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def estudiantes(request):
    estudiantes = estudiante.objects.all()
    return render(request, 'estudiantes/index.html', {'estudiantes':estudiantes})

def crear(request):
    formulario = estudianteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('estudiantes')
    return render(request, 'estudiantes/crear.html', {'formulario':formulario})

def editar(request, id):
    estudianteE = estudiante.objects.get(id=id)
    formulario= estudianteForm(request.POST or None, request.FILES or None, instance=estudianteE)
    if formulario.is_valid():
        formulario.save()
        return redirect('estudiantes')
    return render(request, 'estudiantes/editar.html',{'formulario': formulario})

def eliminar(request, id):
    estudianteD = estudiante.objects.get(id=id)
    estudianteD.delete()
    return redirect("estudiantes")

