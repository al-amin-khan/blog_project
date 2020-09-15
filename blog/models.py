from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(blank=False, max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField(blank=False)

    def __str__(self):
        return self.title
