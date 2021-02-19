from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify
import os
from django.conf import settings

# Create your models here.

class Pokemon(models.Model):

    name = models.CharField(max_length=30)
    description = models.TextField()
    ability_1 = models.CharField(max_length=20)
    ability_2 = models.CharField(max_length=20, blank=True)
    category_1 = models.CharField(max_length=20)
    category_2 = models.CharField(max_length=20, blank=True)
    img = models.CharField(max_length=50, blank=True)

    height = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)

    slug = models.SlugField(null=True, unique=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('pokemon_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        if not self.img:
            self.img = f'/img/official-artwork/{self.id}.png'
            self.save()
    