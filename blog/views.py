from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.utils import timezone
from django.core.paginator import Paginator

from .models import Post


# Create your views here.
def post_list(request):
    posts_list = Post.published.all()
    paginator = Paginator(posts_list, 1)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)

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
