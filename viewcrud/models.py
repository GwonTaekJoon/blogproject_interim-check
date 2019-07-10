from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]


class Comment(models.Model):
    post = models.ForeignKey('viewcrud.Blog', on_delete=models.CASCADE,related_name='comments')
    author=models.CharField(max_length=200)
    text=models.TextField()
    approved_comment=models.BooleanField(default=False)

    def approved(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


