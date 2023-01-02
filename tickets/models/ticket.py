from django.db import models
from django.utils.translation import gettext_lazy as _
from django.forms import EmailInput
from tickets.util import places


class TravelClass(models.TextChoices):
    ECONOMY = 'ECON', _('Economy')
    BUSINESS = 'BUSS', _('Business')
    FIRST_CLASS = 'FIRS', _('First Class')


class Places(models.TextChoices):
    SP = 'SP', _('São Paulo'),
    MG = 'MG', _('Minas Gerais'),
    BA = 'BA', _('Bahia'),
    RJ = 'RJ', _('Rio de Janeiro'),
    SC = 'SC', _('Santa Catarina')


class Ticket(models.Model):
    origin = models.CharField(max_length=25, choices=Places.choices)
    destiny = models.CharField(max_length=25, choices=Places.choices)
    start_date = models.DateField()
    end_date = models.DateField()
    search_date = models.DateField()
    information = models.TextField(max_length=200, blank=True)
    travel_class = models.CharField(max_length=15, choices=TravelClass.choices, default=0)
    urgent = models.BooleanField()
    scale = models.DecimalField(decimal_places=0, max_digits=1)

    # origin = ChoiceField(label='Origin', choices=places)  # css in html
    # destiny = ChoiceField(label='Destiny', choices=places, widget=Select(attrs={'class': 'form-control'}))
    # start_date = DateField(label='Start', widget=DatePicker())
    # end_date = DateField(label='End', required=False, widget=DatePicker())
    # search_date = DateField(label='Search Date', disabled=True, initial=datetime.today, widget=DatePicker())
    # travel_class = ChoiceField(label='Travel Class', choices=travel_classes,
    #                            widget=Select(attrs={'class': 'form-control'}))
    # information = CharField(label='Extra Information', max_length=200, widget=Textarea(attrs={'class': 'form-control'}))
    # email = EmailField(label='E-mail', required=False, max_length=150, widget=EmailInput(attrs={'class': 'form-control'}))
    # urgent = BooleanField(label='Urgent?!', required=False, widget=CheckboxInput(attrs={'class': 'form-control'}))
    # scale = DecimalField(label='How much urgent: 1 - 5', required=False, widget=NumberInput(attrs={'class': 'form-control'}))