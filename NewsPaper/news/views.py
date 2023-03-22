from django.views.generic import ListView,DetailView
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Post

# Create your views here.
class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10


class NewDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'

class Search(ListView):
    template_name = 'search.html'
    model = Post