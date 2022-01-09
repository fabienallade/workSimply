from django.db import models

from categories.models import Category


def upload_post_image(instance, filename):
    return "products/images/{filename}".format(filename=filename)


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=500)
    price = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(Category, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to=upload_post_image, null=False)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
