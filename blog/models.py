from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'df', 'draft'
        PUBLISHED = 'pb', 'published' 


    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    body = models.TextField()
    publish_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.DRAFT
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )

    objects = models.Manager()
    published = PublishedManager()


    class Meta:
        ordering = ('-publish_at',)
        indexes = [
            models.Index(fields=['publish_at'], name='publish_idx'),
        ]


    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[
            self.publish_at.year,
            self.publish_at.month,
            self.publish_at.day,
            self.slug
        ])


    def __str__(self):
        return f'{self.title}'
