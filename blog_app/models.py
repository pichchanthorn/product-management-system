from pyexpat import model
from django import db
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.TextField(max_length=30, null=False, blank=False, unique=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'tbl_category'
        
class Product(models.Model):
    ProductId = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=150, null=False, blank=False)
    Barcode = models.CharField(max_length=50, unique=True, null=True, blank=True)
    Price = models.FloatField(null=False)
    Cost = models.FloatField(null=True, blank=True)
    Qty = models.IntegerField(null=True, blank=True)
    Unit = models.CharField(max_length=50, null=True, blank=True)
    Description = models.CharField(max_length=500, null=True, blank=True)
    CategoryId = models.ForeignKey(
        'Category',
        on_delete=models.RESTRICT,
        db_column='CategoryId',
        null=False
    )
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'tbl_product'