from datetime import datetime
from django.forms import Form, CharField, DateField, TextInput, ChoiceField, Select, Textarea, BooleanField, CheckboxInput, DecimalField, NumberInput, EmailField, EmailInput, ValidationError
from tempus_dominus.widgets import DatePicker
from tickets.util import validate_origin_destiny, validate_start_end_dates, validate_start_date, scale_correct
from tickets.models import travel_classes, places


class TicketForms(Form):
    origin = ChoiceField(label='Origin', choices=places)  # css in html
    destiny = ChoiceField(label='Destiny', choices=places, widget=Select(attrs={'class': 'form-control'}))
    start_date = DateField(label='Start', widget=DatePicker())
    end_date = DateField(label='End', required=False, widget=DatePicker())
    search_date = DateField(label='Search Date', disabled=True, initial=datetime.today, widget=DatePicker())
    travel_class = ChoiceField(label='Travel Class', choices=travel_classes,
                               widget=Select(attrs={'class': 'form-control'}))
    information = CharField(label='Extra Information', max_length=200, widget=Textarea(attrs={'class': 'form-control'}))
    email = EmailField(label='E-mail', required=False, max_length=150, widget=EmailInput(attrs={'class': 'form-control'}))
    urgent = BooleanField(label='Urgent?!', required=False, widget=CheckboxInput(attrs={'class': 'form-control'}))
    scale = DecimalField(label='How much urgent: 1 - 5', required=False, widget=NumberInput(attrs={'class': 'form-control'}))

    def clean_information(self):
        information = self.cleaned_data.get('information')
        if any(char.isdigit() for char in information):
            print("---------------------------")
            print(f"{information = }")
            print("---------------------------")
            raise ValidationError('Extra information is invalid! No digits (?!) allowed.')
        else:
            return information

    def clean(self):
        error_list = {}

        if not validate_origin_destiny(self.cleaned_data.get('origin'), self.cleaned_data.get('destiny')):
            error_list['destiny'] = "Origin and destiny can't be equal!!"

        if validate_start_end_dates(self.cleaned_data.get('start_date'), self.cleaned_data.get('end_date')):
            error_list['end_date'] = "Start/End Date is invalid!!"

        if validate_start_date(self.cleaned_data.get('start_date'), self.cleaned_data.get('search_date')):
            error_list['start_date'] = "Start date can't be before search date!!"

        if not scale_correct(self.cleaned_data.get('scale')):
            error_list['scale'] = "Scale should be 1, 2, 3, 4 or 5!!"

        if error_list is not None:
            for error in error_list:
                self.add_error(error, error_list[error])

        return self.cleaned_data
