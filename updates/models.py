import json

from django.conf import settings
from django.core.serializers import serialize
from django.db import models


def upload_update_image(instance, filename):
    return "updates/{user}/{filename}".format(user=instance.user, filename=filename)


class UpdateQuerySet(models.QuerySet):
    def serialize(self):
        list_values = list(self.values('user', 'content', 'image', 'id'))
        return json.dumps(list_values)


class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model, using=self._db)


# Create your models here.
class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_update_image, blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = UpdateManager()

    def __str__(self):
        return self.content or ""

    def serialize(self):
        try:
            image = self.image
            if self.image.url:
                image = self.image.url
        except:
            image = ""
        data = {
            "content": self.content,
            "user": self.user.id,
            "image": image,
            "id": self.id
        }

        return json.dumps(data)
