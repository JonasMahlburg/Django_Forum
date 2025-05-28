from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from .permissions import IsOwnerOrReadOnly
from forum_app.models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


"""
API view to list all posts or create a new post.
Only authenticated users can create posts.
"""
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
     serializer.save(author=self.request.user)

"""
API view to retrieve, update, or delete a specific post.
Only the author or an admin can update or delete the post.
"""
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]


"""
API view to list all comments or create a new comment.
Only authenticated users can create comments.
"""
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
      serializer.save(author=self.request.user)

"""
API view to retrieve, update, or delete a specific comment.
Only the author or an admin can update or delete the comment.
"""
class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]


