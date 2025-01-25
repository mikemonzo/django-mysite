from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.utils import timezone

from .models import Post


# Create your views here.
def posts_view(request):
    posts = Post.published.all()
    return render(request, 'post/list.html', {'posts': posts})


def post_detail(request, id):
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404(f'Post [{id}] not found.')

    return render(request, 'post/detail.html', {'post': post})
