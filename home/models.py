from django.db import models


# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=100, null=False)
    message = models.TextField()
    email = models.EmailField(default='non', max_length=254,
                              null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self