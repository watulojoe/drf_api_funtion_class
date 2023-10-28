from django.db import models


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(("title"), max_length=25)
    content = models.TextField(("content"))
    date_created  = models.DateTimeField(("date_created"), auto_now_add=True)

    def __str__(self):
        return self.title
    