from . import views 

# we need the path functon to create a url pattern
from django.urls import path

urlpatterns = [
    path('<slug:slug>', views.BlogView.as_view(), name='blog_view')
]

#we tell django to find the dogs slug in each row
#example.com/dogs