from django.db import models
from django.utils.text import slugify


class Department(models.Model):
    dept_title = models.CharField("department", max_length=100, blank=False)
    dept_slug = models.SlugField()
    dept_desc = models.TextField('desc', blank=True)
    price = models.DecimalField('price', max_digits=10, decimal_places=2, blank=False, null=False, default=0)
    dept_cover = models.ImageField(upload_to="department/cover", blank=True, null=True)
    objects = models.Manager

    def __str__(self):
        return self.dept_title

    def save(self, *args, **kwargs):
        if not self.dept_slug:
            self.dept_slug = slugify(self.dept_title)
        return super().save(*args, **kwargs)
