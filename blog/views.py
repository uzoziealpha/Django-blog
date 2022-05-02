from django.shortcuts import render
#import POST
from .models import Post

from django.views import generic


# Create your views here.

class BlogView(generic.DetailView):
    model = Post
    template_name = 'blog.html'

#we can add more pages like this
class HomeView(generic.TemplateView):
    template_name = 'index.html'
