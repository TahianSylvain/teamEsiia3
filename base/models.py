from django.db import models
from django.utils.text import slugify

# Create your models here.

class Institut(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media\logo_institut",blank=True)
    choice_categories=[
        ("EB","Economics and Business Sciences"),
        ("HS","Health Sciences"),
        ("ES","Engineering Sciences"),
    ]
    categorie = models.CharField(max_length=2, choices=choice_categories,blank=True)
    desription = models.TextField()

    class Meta:
        verbose_name = ('Institut')
        verbose_name_plural = ('Instituts')
    def __str__(self):
        return self.name