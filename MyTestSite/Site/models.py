from django.contrib.auth.models import User
from django.db import models

SHOT_TEXT_LEN = 1000

class Articles(models.Model):
    title = models.CharField(max_length=200)
    Text = models.TextField()
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_shot_text(self):
        if len(self.text) > SHOT_TEXT_LEN:
            return self.text[:SHOT_TEXT_LEN]
        else:
            return self.text

