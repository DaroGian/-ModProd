from django.shortcuts import render
from AppCoder.models import Cursos, cursoform
from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.forms import cursoform

def inicio(req):
    return render(req, 'AppCoder/inicio.html')

def cursos(req):
    lista = Cursos.objects.all()
    return render(req, 'AppCoder/cursos.html', {"Lista": lista})

def profesores(req):
    return render(req, 'AppCoder/profesores.html')

def estudiantes(req):
    return render(req, 'AppCoder/estudiantes.html')

def entregables(req):
    return render(req, 'AppCoder/entregables.html')

def cursoform(request):
    
    if(request.method == 'POST'):
        
        miformulario = cursoform(request.POST)
        
        print(miformulario)
        
        if (miformulario.is_valid()):
            
            info=miformulario.cleaned_data
            
            curso = Cursos(nombre=info["curso"], camada=info["camada"])
            curso.save()
            
            return render (request, "AppCoder/inicio.html")
        else:
            return HttpResponse('FORM NO VALIDO')
    
    else:
        miformulario = cursoform()
        
    return render(request, "AppCoder/cursoform .html", {'form': miformulario}) 
