from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.utils import timezone

from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.published.all()
    return render(request, 'post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    try:
        post = Post.published.get(
            slug=post,
            publish_at__year=year,
            publish_at__month=month,
            publish_at__day=day
        )
    except Post.DoesNotExist:
        raise Http404(f'Post [{id}] not found.')

    return render(request, 'post/detail.html', {'post': post})
