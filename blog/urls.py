from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.posts_view, name='posts_view'),
    path('<int:id>/', views.post_detail, name='post_detail'),
]
