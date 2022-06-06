#models = modules
from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
  #class attributes/ columnes db-table
  title = models.CharField(max_length=255) #title extends form charfield
  body = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('post_detail', args=[self.id])