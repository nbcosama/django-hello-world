from django.db import models


class Supply(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    supplier = models.CharField(max_length=100)

    def __str__(self):
        return self.item_name
