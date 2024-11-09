from django.urls import path
from .views import HomePageView, UsuarioView, UpdatePageView, DeletePageView
from .views import CreateView, DetailView

urlpatterns= [

    path("",HomePageView.as_view(), name = "post"),
    path("usuarios",UsuarioView.as_view(), name = "usuarios"),
    path("post/create",CreateView.as_view(), name = "create"),
    path("post/detail/<int:pk>",DetailView.as_view(), name="detail"),
    path("post/detail/<int:pk>/update",UpdatePageView.as_view(), name="update"),
    path("post/detail/<int:pk>/delete",DeletePageView.as_view(), name="delete")
]
    


