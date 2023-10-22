# blog/models.py
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog', blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='blog', blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]
    
    def get_absolute_url(self):
        return reverse('blog:blog_post_detail', kwargs={'pk': self.pk})
    
    def total_likes(self):
        return self.likes.count()
   
class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=100)
    comment_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.comment_text
    
    def approve(self):
        self.approved = True
        self.save()



    

