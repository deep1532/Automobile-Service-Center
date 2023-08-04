from django.db import models

class EmpModel(models.Model):
    customer_id = models.CharField(max_length=100, primary_key=True)
    customer_name = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    class Meta:
        db_table = '"as_db"."customer"'


class OfferModel(models.Model):
    offer_id = models.CharField(max_length=100, primary_key=True)
    service_id = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    discount_percentage = models.BigIntegerField()
    max_discount = models.BigIntegerField()
    class Meta:
        db_table = '"as_db"."offers"'