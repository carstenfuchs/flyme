from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Q
from django.shortcuts import render

from Organizations.models import Membership, Ability
from Aviation.models import Flight, Reservation


@login_required
@transaction.non_atomic_requests
def view(request):
    u = request.user

    return render(request, "Organizations/user_overview.html", {
        "flights": Flight.objects.filter(Q(pic=u) | Q(co=u)),
        "abilities": Ability.objects.filter(user=u),
        "reservations": Reservation.objects.filter(user=u),
        "memberships": Membership.objects.filter(user=u),
    })
