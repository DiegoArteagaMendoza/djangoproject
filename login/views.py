from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, CreateNewUser
from .models import Users
from django.contrib.auth.hashers import make_password, check_password

def create_user(request):
    if request.method == 'GET':
        return render(request, 'register.html', {
            'form': CreateNewUser()
        })
    else:
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            hashed_password = make_password(password)  # Cifra la contraseña antes de guardarla
            Users.objects.create(
                username=request.POST['username'],
                password=hashed_password
            )
            return redirect('/home/')  # Asegúrate de que esta URL exista
        else:
            return HttpResponse("Las contraseñas no coinciden")


def login(request):
    title = 'Login'
    if request.method == 'GET':
        return render(request, 'login.html', {
            'title': title,
            'form': LoginForm()
        })
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = Users.objects.get(username=username)
            if check_password(password, user.password):  # Verifica la contraseña cifrada
                return redirect('/home/')  # Asegúrate de que esta URL exista
            else:
                return HttpResponse("Credenciales incorrectas")
        except Users.DoesNotExist:
            return HttpResponse("Usuario no encontrado")
