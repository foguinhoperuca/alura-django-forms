from django.shortcuts import render
from tickets.forms import TicketForms


def index(request):
    form = TicketForms()
    context = {'form': form}

    return render(request, 'tickets/index.html', context)


def my_travels(request):
    if request.method == 'POST':
        form = TicketForms(request.POST)
        destiny = 'tickets/my_travels.html'
        ctx = {'form': form}

        if not form.is_valid():
            destiny = 'tickets/index.html'
            print('Form invalid!')

        return render(request, destiny, ctx)
