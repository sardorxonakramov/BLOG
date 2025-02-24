from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from .models import Post
from .forms import PostForm
# Create your views here.


class PostLView(ListView):
    model = Post
    template_name = 'POST_APP/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class DetailPView(DetailView):
    model = Post
    pk_url_kwarg = 'post_id'
    template_name = 'POST_APP/detail.html'
    context_object_name = 'post'
    ordering = ['-date_posted']

class CreatePView(CreateView):
    model = Post
    template_name = 'POST_APP/create.html'
    form_class = PostForm
    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'post_id': self.object.id})
    
class UpdatePView(UpdateView):
    model = Post
    template_name = 'POST_APP/update.html'
    form_class = PostForm
    pk_url_kwarg = 'post_id'
    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'post_id': self.object.id})
    
class DeletePView(DeleteView):
    model = Post
    template_name = 'POST_APP/delete.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'
    success_url = reverse_lazy('home')
    