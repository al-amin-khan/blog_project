from django.db import models
from django.urls import reverse
# from django.utils import timezone
from autoslug import AutoSlugField

# Create your models here.
class Post(models.Model):
    title = models.CharField(blank=False, max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField(blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from=lambda instance: instance.title,
                         unique_with=['title', 'author'],
                         slugify=lambda value: value.replace(' ','-'),
                          )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug':self.slug})
