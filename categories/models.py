from django.db import models


def upload_post_image(instance, filename):
    return "images/categories/{filename}".format(filename=filename)

    # Create your models here.


class Category(models.Model):
    ICONS_IN_ICON_CHOICES = [
        ('APPS', 'apps'),
        ('LAN', 'lan'),
        ('ADJUST', 'adjust'),
        ('ADOBE', 'adobe'),
        ('AIR_HORN', 'air-horn')
    ]
    COLORS_CHOICES = [
        ('BLUE', 'blue'),
        ('GREEN', 'green'),
        ('ORANGE', 'orange'),
        ('gray', 'gray'),
        ('BLACK', 'black')
    ]

    name = models.TextField()
    icon = models.CharField(max_length=12, choices=ICONS_IN_ICON_CHOICES, default=ICONS_IN_ICON_CHOICES[0])
    color = models.CharField(max_length=12, choices=COLORS_CHOICES, default=COLORS_CHOICES[0])
    image = models.ImageField(upload_to=upload_post_image, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
