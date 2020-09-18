from django.db import models

class ProductData(models.Model):
    Product_id = models.IntegerField(unique=True)
    Product_name = models.CharField(max_length=100)
    Price = models.IntegerField()
    Cname = models.CharField(max_length=100)
    Mobile = models.BigIntegerField()



