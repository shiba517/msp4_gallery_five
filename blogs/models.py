from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=80)
    article = models.TextField()
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.writing[:100] + '...'
