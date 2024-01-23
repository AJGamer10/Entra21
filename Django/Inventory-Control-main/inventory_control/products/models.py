from django.db import models
from django.utils.text import slugify

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    sale_price = models.DecimalField(max_digits=12, decimal_places=2)
    is_perishable = models.BooleanField(default=True)
    expiration_date = models.DateField()
    photo = models.ImageField(upload_to='products-images')
    enabled = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        
        super(Product, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
