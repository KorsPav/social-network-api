from django.db import models

from user.models import SNUser
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField(max_length=1000)
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(SNUser, on_delete=models.CASCADE, null=False)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(max_length=100, unique=True, default='', editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(SNUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.post.likes += 1
        self.post.save()
        super(Like, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.post.likes -= 1
        self.post.save()
        super(Like, self).delete(*args, **kwargs)

    class Meta:
        unique_together = ('user', 'post')
