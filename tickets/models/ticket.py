from django.db import models


class TravelClass(models.TextChoices):
    ECONOMY = 'ECON', _('Economy')
    BUSINESS = 'BUSS', _('Business')
    FIRST_CLASS = 'FIRST', _('First Class')


class Ticket(models.Model):
    origin = models.CharField(max_length=100)
    destiny = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    search_date = models.DateField()
    extra_information = models.TextField(max_length=200, blank=True)
    travel_class = models.CharField(max_length=4, choices=TravelClass.choices, default=0)
