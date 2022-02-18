from django.db import models

# Create your models here.

class Episode(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField("pubDate")
    description = models.TextField()
    url = models.URLField()
    length = models.IntegerField()

    class Meta:
        ordering = ["pub_date"]

    def __str__(self):
        return self.title

