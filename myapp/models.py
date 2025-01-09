# crear clases que se confierten en tablas sql
from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title + ' - ' + self.project.name
    
class Employees(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    salary = models.IntegerField()
    
    def __srt__(self):
        return self.name + ' - ' + self.last_name