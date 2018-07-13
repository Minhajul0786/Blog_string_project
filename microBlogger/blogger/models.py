from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    username = models.ForeignKey(User,on_delete='CASCADE')
    content = models.TextField()

    def __str__(self):
        return str(self.pk)

class Comment(models.Model):
    username = models.ForeignKey(User,on_delete='CASCADE')
    blogtext = models.ForeignKey(Blog,on_delete='CASCADE')
    content = models.CharField(max_length=264)

    def __str__(self):
        return str(self.pk)
