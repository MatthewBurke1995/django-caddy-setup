from django.db import models

# Create your models here.


class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_date = models.DateTimeField("date published")
    post_text = models.TextField()

    def summary(self):
        return self.post_text.split("\n")[0]
    
    class Meta:
        ordering = ["post_date"]

    def __str__(self):
        return self.post_title


class Tag(models.Model):
    tag = models.CharField(max_length=50)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return self.tag
