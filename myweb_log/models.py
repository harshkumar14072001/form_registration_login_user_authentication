from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=20)
    text=models.TextField()

    def __str__(self):
        self.title
# Create your models here.
