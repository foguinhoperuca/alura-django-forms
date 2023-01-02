from datetime import datetime
from django.forms import ModelForm, CharField, DateField, TextInput, ChoiceField, Select, Textarea, BooleanField, CheckboxInput, DecimalField, NumberInput, EmailField, EmailInput, ValidationError
from tempus_dominus.widgets import DatePicker
from tickets.util import validate_origin_destiny, validate_start_end_dates, validate_start_date, scale_correct, places
from tickets.models import Ticket, Person


class TicketForms(ModelForm):
    search_date = DateField(label='Search Date', disabled=True, initial=datetime.today, widget=DatePicker())

    class Meta:
        model = Ticket
        fields = '__all__'
        labels = {
            'start_date': 'Start Date',
            'end_date': 'End Date',
            'travel_class': 'Travel Class',
            'information': 'Extra Information',
        }
        widgets = {
            'start_date': DatePicker(),
            'end_date': DatePicker()
        }

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


class PersonForms(ModelForm):
    class Meta:
        model = Person
        exclude = ['name']
