from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200, widget=forms.TextInput(attrs={'class':'input'}))
    description = forms.CharField(label="Descripcion de la tarea", widget=forms.Textarea(attrs={'class':'input'}))
    
class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del proyecto", max_length=200, widget=forms.TextInput(attrs={'class':'input'}))
    
class CreateNewEmployee(forms.Form):
    name = forms.CharField(label="Nombre del empleado",max_length=200, widget=forms.TextInput(attrs={'class':'input'}))
    last_name = forms.CharField(label="Apellido del empleado",max_length=200, widget=forms.TextInput(attrs={'class':'input'}))
    position = forms.CharField(label="Cargo del empleado",max_length=200, widget=forms.TextInput(attrs={'class':'input'}))
    start_date = forms.DateTimeField(label="Fecha de inicio", widget=forms.TextInput(attrs={'class':'input'}))
    salary = forms.IntegerField(label="Sueldo", widget=forms.TextInput(attrs={'class':'input'}))