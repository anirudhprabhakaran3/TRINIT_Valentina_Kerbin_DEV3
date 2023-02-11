from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title

    def return_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    datestamp = models.DateTimeField(default=timezone.now)


class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
