from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .form import PostForm, EditForm
from django.urls import reverse_lazy
# Create your views here.

# def index(request):
#     return render(request,'index.html')

class HomeView(ListView):
    model=Post
    template_name= 'home.html'
    #ordering=['created_at']
    
class ArticleDetailView(DetailView):
    model=Post
    template_name='article_details.html'

class AddPostView(CreateView):
    model=Post
    form_class= PostForm
    template_name='add_post.html'  
    #fields= '__all__'
    #fields= ('title','title_tag','author','body') 

class UpdatePostView(UpdateView):
    model = Post
    form_class= EditForm
    template_name = "update_post.html"
    #fields=['title','title_tag','author','body','created_at']

class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url= reverse_lazy('home')