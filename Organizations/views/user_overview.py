from datetime import date
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render


@login_required
@transaction.non_atomic_requests
def view(request):
    heute = date.today()

    return render(request, "Organizations/user_overview.html", {
        "heute": heute,
    })
