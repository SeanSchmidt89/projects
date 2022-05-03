from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import *

# Create your views here.

class Index(ListView):
    model = Todo
    template_name = 'todo_app/index.html'
    context_object_name = 'todos'

class TodoDetail(DetailView):
    model = Todo
    template_name = 'todo_app/todo.html'
    context_object_name = 'todo'

class TodoUpdate(UpdateView):
    model = Todo
    fields = '__all__'
    template_name = 'todo_app/update.html'
    success_url = reverse_lazy('index')

class TodoDelete(DeleteView):
    model = Todo
    template_name = 'todo_app/delete.html'
    context_object_name = 'todo'
    success_url = reverse_lazy('index')

class TodoCreate(CreateView):
    model = Todo
    fields = "__all__"
    template_name = 'todo_app/create.html'
    context_object_name = 'form'
    success_url = reverse_lazy('index')