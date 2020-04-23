from django.db import models

# Create your models here.
class ProductManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id) # Product.objects.filter()
        if(qs.count() == 1):
            return qs.first()
        else:
            return None
    
    def get_product_list(self):
        qs = self.get_queryset().all()
        if(qs.count() == 0):
            return None
        else:
            return qs

    def get_by_featured(self, id, featured):
        qs = self.get_queryset().filter(id=id, featured=featured)
        if(qs.count() == 1):
            return qs.first()
        else:
            return None
    
    def get_featured_list(self):
        qs = self.get_queryset().filter(featured=True)
        if(qs.count() == 0):
            return None
        else:
            return qs

class Product(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    featured = models.BooleanField(default=False)

    objects = ProductManager()

    def __str__(self):
        return self.title
    