from django.db import models


class Company(models.Model):
    name = models.CharField(db_index=True, max_length=40)
    address = models.CharField(max_length=100)
    tax_id = models.CharField(max_length=30)
    country = models.CharField(max_length=3)
    phone = models.CharField(max_length=26)
