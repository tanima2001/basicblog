from django.urls import path
from .views import UserRegisterView
#from .views import HomeView,ArticleDetailView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
]

