from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

class Post(models.Model):
    OPTIONS = (
        ('Draft' , 'Draft'),
        ('Published','Published'),
    )
    title = models.CharField(max_length=250,null=False)
    subtitle = models.CharField(max_length=250,null=False)
    slug = models.SlugField(max_length=250, unique=True)
    content = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=OPTIONS, default='Draft')
    
    tags = TaggableManager()
    
    def get_absolute_url(self):
        return reverse('post_single', args=[self.slug])
    
    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        
    def __str__(self):
        return self.title
