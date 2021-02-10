from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Pokemon(models.Model):

    name = models.CharField(max_length=30)
    description = models.TextField()
    ability_1 = models.CharField(max_length=20)
    ability_2 = models.CharField(max_length=20)
    category_1 = models.CharField(max_length=20)
    category_2 = models.CharField(max_length=20)
    img = models.FilePathField(path='')

    height = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['id']


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return(reverse('pokemon_detail', args=[str(self.id)]))