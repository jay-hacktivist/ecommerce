import random
import os
from django.db import models
# from django.db.models import Model
# Create your models here.


def get_filename_ext(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    # print(instance)
    # print(filename)
    new_filename = random.randint(1, 4568618454)
    _, ext = get_filename_ext(filename)
    # .format(new_filename=new_filename, ext=ext)
    final_filename = f'{new_filename}{ext}'
    return "products/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
    )


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=19, default=0.00)
    image = models.ImageField(
        upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return self.title
