from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,CreateView,DeleteView
from . import models
from django.urls import reverse_lazy
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class TodoListView(ListView):
    context_object_name = 'todolist'
    model = models.Todo

class TodoUpdateView(UpdateView):
    fields = '__all__'
    model = models.Todo

class TodoDetailView(DetailView):
    context_object_name = "tododetail"
    model = models.Todo
    template_name = 'todo_app/todo_detail.html'

class TodoCreateView(CreateView):
    fields = '__all__'
    model = models.Todo

class TodoDeleteView(DeleteView):
    model = models.Todo
    success_url = reverse_lazy('todo_app:list')
