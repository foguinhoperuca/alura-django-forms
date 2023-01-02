from django.shortcuts import render
from tickets.forms import TicketForms, PersonForms


def index(request):
    form = TicketForms()
    person_form = PersonForms()
    context = {
        'form': form,
        'person_form': person_form
    }

    return render(request, 'tickets/index.html', context)


def my_travels(request):
    if request.method == 'POST':
        form = TicketForms(request.POST)
        person_form = PersonForms(request.POST)
        destiny = 'tickets/my_travels.html'
        ctx = {
            'form': form,
            'person_form': person_form
        }

        if not form.is_valid():
            destiny = 'tickets/index.html'
            print('Form invalid!')

        return render(request, destiny, ctx)
