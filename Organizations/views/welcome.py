from datetime import date
from django.db import transaction
from django.shortcuts import render


@transaction.non_atomic_requests
def view(request):
    heute = date.today()

    return render(request, "Organizations/welcome.html", {
        "heute": heute,
    })
