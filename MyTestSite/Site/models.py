from django.contrib.auth.models import User
from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=200)
    Text = models.TextField()
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title

