from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # Corrige el slash inicial
    path('about/', views.about),
    path('hello/<str:username>/', views.hello),  # Agrega el slash al final para consistencia
    path('projects/', views.projects),
    path('task/', views.task),
    path('create_task/', views.create_task),
    path('create_project/', views.create_project),
    path('projects/<int:id>/', views.projects_detail, name="project_detail"),
    path('create_employees/', views.create_employee),  # Corrige el espacio extra
    path('employees/', views.employees),
]
