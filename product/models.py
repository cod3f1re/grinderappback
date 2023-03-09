from django.db import models
from django.db.models import UniqueConstraint


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField()

    class Meta:
        db_table = 'category'  # Le doy de nombre 'Category' a nuestra tabla en la Base de Datos

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    percentage_discount = models.FloatField(blank=True, null=True)
    description = models.TextField()
    slug = models.SlugField()
    date_inactive = models.DateField()
    active = models.BooleanField()
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product'  # Le doy de nombre 'product' a nuestra tabla en la Base de Datos

    def __str__(self):
        return "%s %s %s" % (self.title, self.price, self.description)


class Customer(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    address1 = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100)
    purchases_completed = models.CharField(max_length=100)

    class Meta:
        db_table = 'customer'  # Le doy de nombre 'customer' a nuestra tabla en la Base de Datos

    def __str__(self):
        return "%s %s %s" % (self.name, self.last_name, self.email)


class Order(models.Model):
    orderDate = models.DateField()
    requiredDate = models.DateField()
    shippedDate = models.DateField()
    status = models.CharField(max_length=20)
    comments = models.CharField(max_length=200)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        db_table = 'order'  # Le doy de nombre 'order' a nuestra tabla en la Base de Datos

    def __str__(self):
        return "%s %s %s" % (self.orderDate, self.shippedDate, self.status)


class OrderDetail(models.Model):
    num_detail = models.CharField(max_length=30)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        db_table = 'orderDetail'  # Le doy de nombre 'orderDetail' a nuestra tabla en la Base de Datos
        UniqueConstraint(fields=['num_detail', 'order'], name='num_detail_primarys')

    def __str__(self):
        return "%s %s %s" % (self.num_detail, self.price, self.order)
