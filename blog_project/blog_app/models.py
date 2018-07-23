from django.db import models
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    image = models.FileField(blank=True,null=True)
    content = models.TextField(max_length=300)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('posts:detail',args=[self.pk])
    class Meta:
        ordering = ["-timestamp","-updated"]
