from django.db import models

class Event(models.Model):
    """
    Client model
    """
    client = models.CharField(max_length=200, null=False, blank=False)
    address_line_one = models.CharField(max_length=200, null=False, blank=False)
    address_line_two = models.CharField(max_length=200, null=True, blank=True)
    county = models.CharField(max_length=200, null=False, blank=False)
    country = models.CharField(max_length=200, null=False, blank=False)
    paid_to_date = models.DecimalField(max_digits=20, decimal_places=2)
    balance = models.DecimalField(max_digits=20, decimal_places=2)
    email = models.CharField(max_length=200, null=False, blank=False)

    class Meta:
        ordering = ['client']

    def __str__(self):
        return self.client