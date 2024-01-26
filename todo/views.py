from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import TodoModel

# Create your views here.

class todolist(ListView):
    template_name = 'list.html'
    model = TodoModel


class tododetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel