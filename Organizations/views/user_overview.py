from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import F, Q
from django.shortcuts import render

from Aviation.models import Flight, Reservation
from Organizations.common import get_managed_user
from Organizations.models import Membership, Ability


@login_required
@transaction.non_atomic_requests
def view(request, user_id=None):
    mu = get_managed_user(request.user, user_id)

    return render(request, "Organizations/user_overview.html", {
        "mu": mu,
        "flights": Flight.objects.filter(Q(pic=mu) | Q(co=mu)),
        "abilities": Ability.objects.filter(user=mu).order_by(F('expires').asc(nulls_last=True), 'kind'),
        "reservations": Reservation.objects.filter(user=mu),
        "memberships": Membership.objects.filter(user=mu),
    })
