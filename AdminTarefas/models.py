from django.db import models
from django import forms

# Crie um modelo de dados para representar as tarefas que os usuários podem criar e gerenciar.
class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
    description = models.TextField(max_length=200)
    def __str__(self):
        return self.title
        
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']