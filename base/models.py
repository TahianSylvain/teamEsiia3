from django.db import models
from django.utils.text import slugify

# Create your models here.

class Institut(models.Model):
    name = models.TextField()
    image = models.ImageField(upload_to='images',blank=True)
    choice_categories=[
        "Economics and Business Sciences",
        "Health Sciences",
        "Engineering Sciences",
    ]
   # categorie = models.CharField(max_length=50, choices=choice_categories)
    desription = models.TextField()

    class Meta:
        verbose_name = ('Institut')
        verbose_name_plural = ('Instituts')
    def __str__(self):
        return self.name