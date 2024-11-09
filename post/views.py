from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Personas 
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import DetailView 
from django.views.generic.edit import DeleteView,UpdateView

# Create your views here.
class HomePageView(ListView):
    template_name = "post.html"
    model = Post

class UsuarioView(ListView):
    template_name = "usuarios.html"
    model = Personas 

class CreateView(CreateView):
     
    model=Post
    template_name="create.html"
    fields=["titulo","descripcion","imagen","precio"]
    success_url = reverse_lazy("post")

class DetailView(DetailView):

    model=Post
    template_name="detail.html"

class UpdatePageView(UpdateView):
    template_name="update.html"
    model=Post
    fields=["titulo","descripcion","imagen","precio"]
    success_url=reverse_lazy("post")

class DeletePageView(DeleteView):
    template_name="delete.html"
    model=Post
    success_url=reverse_lazy("post")
