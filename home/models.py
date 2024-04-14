from django.db import models

# Create your models here.


class Headline(models.Model):
  title = models.CharField(max_length=200)
  image = models.URLField(null=True, blank=True)
  description=models.CharField(max_length=5000 )
  category=models.CharField(max_length=50)
  url = models.TextField()
  def __str__(self):
    return self.title