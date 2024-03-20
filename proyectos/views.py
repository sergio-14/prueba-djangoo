from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import program
from .forms import proForm


# Create your views here.


def home(request):
    return render(request, 'home.html')


def base(request):

    if request.method == 'GET':
        return render(request, 'base.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('poryectos')
            except IntegrityError:
                return render(request, 'base.html', {
                    'form': UserCreationForm,
                    "error": 'User ya existe'
                })
        return render(request, 'base.html', {
            'form': UserCreationForm,
            "error": 'la contraseña no concide'
        })


def poryectos(request):
    return render(request, 'poryectos.html')

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET' :
        return render(request, 'signin.html', {
        'form': AuthenticationForm
    })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])
        if user is None:
            return render(request, 'signin.html',{
                'form': AuthenticationForm,
                'error': 'Usuario y contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('poryectos')

def programadores(request):
    programadores = program.objects.all()
    return render(request, 'programadores/index.html',{'programadores': programadores})

def crear(request):
    formulario = proForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('programadores')
    return render(request, 'programadores/crear.html',{'formulario': formulario})

def editar(request, id):
    programa = program.objects.get(id=id)
    formulario = proForm(request.POST or None, request.FILES or None, instance=programa)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('programadores')
    return render(request, 'programadores/editar.html',{'formulario': formulario})

def form(request):
    return render(request, 'programadores/form.html')

def eliminar(request, id):
    programa = program.objects.get(id=id)
    programa.delete()
    return redirect('programadores')

