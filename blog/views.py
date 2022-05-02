from django.shortcuts import render
#import POST
from .models import Post

from django.views import generic


# Create your views here.

class BlogView(generic.DetailView):
    model = Post
    template_name = 'blog.html'

#we can add more pages like this
#class HomeView(generic.TemplateView):
#    template_name = 'index.html'

#we can add more pages like this
class AboutView(generic.TemplateView):
    template_name = 'about.html'

#allows us to post multiple times
#status = 1 referes to models.py (status) to show only post that are valid
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('date_created')
    template_name = 'index.html'