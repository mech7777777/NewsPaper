from django.views.generic import ListView,DetailView
from django.shortcuts import render
from django.core.paginator import Paginator

from .filters import PostFilter
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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context
    def post(self,request,*args,**kwargs):
        