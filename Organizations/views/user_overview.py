from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import F, Q
from django.shortcuts import render

from Aviation.models import Flight, Reservation
from Organizations.common import get_relevant_user_or_404
from Organizations.models import Membership, Ability


@login_required
@transaction.non_atomic_requests
def view(request, user_id=None):
    u = get_relevant_user_or_404(request, user_id)

    return render(request, "Organizations/user_overview.html", {
        "u": u,
        "flights": Flight.objects.filter(Q(pic=u) | Q(co=u)),
        "abilities": Ability.objects.filter(user=u).order_by(F('expires').asc(nulls_last=True), 'kind'),
        "reservations": Reservation.objects.filter(user=u),
        "memberships": Membership.objects.filter(user=u),
    })
