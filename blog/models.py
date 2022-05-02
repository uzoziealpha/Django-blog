from django.db import models
from django.contrib.auth.models import User

#allows user to add content in  draft or publish
STATUS = ((0, 'Draft'), (1, 'Publish'))

# Create your models here.

class Post(models.Model):
    #it contains field of data thats stored in a post table
    title = models.CharField(max_length=200)
    content = models.TextField()
    #this will create the recent date and time in the model table when the user clicks
    date_created = models.DateTimeField(auto_now_add=True)
    # slug will be / in addition to the URL
    slug = models.SlugField(max_length=200, unique=True)
    #adding authors to get unique keys to match another DB table
    # this will matchg each users ID automatically and 
    #deletes user post with CASCADE
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    # Drop down list of publish or Draft
    status = models.IntegerField(choices=STATUS, default=0)