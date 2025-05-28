from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
Represents a forum post created by a user.
Each post includes a title, content, author, and timestamp of creation.
"""
class Post(models.Model):

    title = models.CharField(max_length=50)
    content = models.TextField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return f"The Post {self.title} is written by {self.author}"

"""
Represents a comment made by a user on a post.
Each comment is linked to a specific post and includes text, author, and timestamp.
"""
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    text = models.TextField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Comment")
        verbose_name_plural = ("Comments")

    def __str__(self):
        return f"The Comments {self.title} is written by {self.author}"