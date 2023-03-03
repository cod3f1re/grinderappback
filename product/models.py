from django.db import models


# Create your models here.
class ProductManager(models.Manager):
    def create_product(self, title, price, discount_price, description, slug, image, date_created, date_modified,
                       date_inactive, active):
        book = self.create(title=title, price=price, discount_price=discount_price, description=description,
                           slug=slug, image=image, date_created=date_created, date_modified=date_modified,
                           date_inactive=date_inactive,
                           active=active)
        # do something with the book
        return book


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    description = models.TextField()
    slug = models.SlugField()
    image = models.ImageField()
    date_created = models.DateField()
    date_modified = models.DateField()
    date_inactive = models.DateField()
    active = models.BooleanField()

    objects = ProductManager()

    class Meta:
        db_table = 'product'  # Le doy de nombre 'jugos' a nuestra tabla en la Base de Datos

    def __str__(self):
        return "%s %s %s" % (self.title, self.price, self.image)


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
