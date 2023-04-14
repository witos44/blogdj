from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from .models import *


class HomeView(ListView):
    model = Post
    #template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_template_names(self):
        if self.request.htmx:
            return 'blog/post-list-elements.html'
        return 'blog/index.html'
    
def post_single(request,slug):
    post = get_object_or_404(Post,slug=slug,status='Published')
    related = Post.objects.filter(author=post.author)[:5]
    context = {
        'post':post,
        'related' :related,
    }
    return render(request, 'blog/single.html',context)