from django.db import models
from batch.models import Batch

# Create your models here.
class Product(models.Model):

    product_name = models.CharField(max_length=1000)
    product_quantity = models.BigIntegerField()
    buying_price = models.BigIntegerField()
    selling_price = models.BigIntegerField()
    profit = models.BigIntegerField()
    percentage_profit = models.BigIntegerField()

    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    

    def __str__(self) -> str:
        return self.product_name