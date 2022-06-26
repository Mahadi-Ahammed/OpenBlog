from django.db import models

# Create your models here.
class MyPost(models.Model):
    Title = models.CharField(max_length=30)
    Content = models.TextField()
    author = models.CharField(max_length=20)
    def __str__(self):
        return self.Title
