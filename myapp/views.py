from django.http import HttpResponse
from .models import Project, Task, Employees
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject, CreateNewEmployee

# Create your views here.
# se define que se quiere ejecutar o enviar al cliente en pantalla, se puede mandar html
def index(request):
    title = 'Django course!!!'
    return render(request, 'index.html', {
        'title':title,
    })

def about(request):
    username = 'diego'
    return render(request, 'about.html', {
        'username': username,
    })

def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" %username)

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects':projects,
    })

def task(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task.html', {
        'tasks': tasks,
    })
    
def create_task(request):
    if request.method == 'GET':
        # show interface
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('/task/')
     
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('/projects/')
    
def projects_detail(request, id):
    # project = Project.objects.get(id=id)
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project':project,
        'tasks':tasks
    })
    
def create_employee(request):
    if request.method == 'GET':
        return render(request, 'employees/create_employee.html', {
            'form': CreateNewEmployee()
        })
    else:
        Employees.objects.create(name=request.POST['name'], last_name=request.POST['last_name'], position=request.POST['position'], start_date=request.POST['start_date'], salary=request.POST['salary'])
        return redirect('/employees/')
    
def employees(request):
    employees = Employees.objects.all()
    return render(request, 'employees/employees.html', {
        'employees':employees,
    })