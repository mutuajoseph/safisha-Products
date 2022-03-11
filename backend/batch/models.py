from django.db import models

# Create your models here.
class Batch(models.Model):

    batch_name = models.CharField(max_length=1000)
    batch_status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.batch_name