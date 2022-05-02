from django.contrib import admin
from .models import Post


#CREARE A NEW CLASS INHERITING FROM MODEL
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'author')

# Register your models and class  here.
admin.site.register(Post, PostAdmin)