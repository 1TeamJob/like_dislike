from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Product(models.Model):
    owner = models.ForeignKey(User, related_name='products_owner' ,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    like = models.ManyToManyField(User, blank=True)
    slug = models.SlugField(blank=True, null=True)
    


    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(args, kwargs)
    

    def __str__(self):
        return self.name
