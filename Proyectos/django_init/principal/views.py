from django.shortcuts import redirect, render
from .models import Persona
from .forms import personaForm

def inicio(request):
    personas = Persona.objects.all()
    contexto ={
        'personas':personas
    }
    return render(request,'index.html',contexto)

def crearPersona(request):
    if request.method == 'GET':
        form = personaForm()
        contexto = {
            'form':form
        }
    else:
        form = personaForm(request.POST)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'crear_persona.html',contexto)

def editarPersona(request,id):
    persona = Persona.objects.get(id=id)
    if request.method == 'GET':
        form = personaForm(instance=persona)
        contexto = {
            'form':form
        }
    else:
        form = personaForm(request.POST,instance=persona)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'crear_persona.html',contexto)

def eliminarPersona(request,id):
    persona = Persona.objects.get(id=id)
    persona.delete()
    return redirect('index') 