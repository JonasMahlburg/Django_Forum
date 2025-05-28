from django.urls import path
from .views import PostListCreateView, PostDetailView, CommentListCreateView, CommentDetailView

urlpatterns = [
    path('posts/', PostListCreateView.as_view()),
    path('posts/<id>', PostDetailView.as_view()),
    path('comments/', CommentListCreateView.as_view()),
    path('comments/<id>', CommentDetailView.as_view()),
]
