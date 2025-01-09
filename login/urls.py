from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),  # Ruta principal para el login
    path('register/', views.create_user, name='register'),  # Ruta para registro de usuarios
]
