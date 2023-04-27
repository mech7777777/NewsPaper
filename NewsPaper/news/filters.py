from django_filters import FilterSet 
from .models import Post,Author
import io
 

class PostFilter(FilterSet):
    class Meta:
        model = Post
        #Filter fields
        queryset = Post.objects.filter
        fields = {'timeCreate': ['gt'],
                   'heading': ['icontains'], 
                   'author':['gt'],
                   }