from django.shortcuts import render
from .models import Post


# Create your views here.

class BlogView:
    model = Post
    tempplate_name = 'blog.html'