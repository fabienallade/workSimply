from django.db import models
from django.conf import settings


def upload_post_image(instance, filename):
    return "updates/{user}/{filename}".format(user=instance.user, filename=filename)


class PostQuerySet(models.QuerySet):
    pass


class StatusManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)


# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to=upload_post_image, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)[:50]

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
