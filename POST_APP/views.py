from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
# Create your views here.


class PostLView(ListView):
    model = Post
    template_name = 'POST_APP/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']