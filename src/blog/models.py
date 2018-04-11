from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags
import markdown

class Category(models.Model):
    DEFAULT_ID = 1
    name = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True, blank=True, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:categories', kwargs={'pk': self.pk})

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:tags', kwargs={'pk': self.pk})

class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    excerpt = models.CharField(max_length=250, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=Category.DEFAULT_ID)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    page_views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_page_views(self):
        self.page_views += 1
        self.save(update_fields=['page_views'])

    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.body))[:54] + '...'
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_time', 'title']




