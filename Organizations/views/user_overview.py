from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import F, Q
from django.shortcuts import get_object_or_404, render

from Accounts.models import User
from Aviation.models import Flight, Reservation
from Organizations.common import get_managed_organizations
from Organizations.models import Membership, Ability


@login_required
@transaction.non_atomic_requests
def personal_view(request):
    # The user is on `overview/`, looking at his own data.
    morgs_qs = get_managed_organizations(request.user)
    u = request.user

    return render(request, "Organizations/personal_overview.html", {
        "flights": Flight.objects.filter(Q(pic=u) | Q(co=u)),
        "abilities": Ability.objects.filter(user=u).order_by(F('expires').asc(nulls_last=True), 'kind'),
        "reservations": Reservation.objects.filter(user=u),
        "memberships": Membership.objects.filter(user=u),
        "organizations": morgs_qs,
    })


@login_required
@transaction.non_atomic_requests
def member_view(request, user_id):
    # The user is a manager and looking at a member's data.
    # (This is usually someone else's data but can also be his own, through a manager's eyes).
    # Note that the member may also be a member in other organizations that the `request.user` is not a manager of.
    morgs_qs = get_managed_organizations(request.user)

    # The manager can only access users that are in one of the organizations that he is responsible for.
    member = get_object_or_404(User, id=user_id, membership__orga__in=morgs_qs)

    # The manager can only see flights that were made with airplanes that he is responsible for.
    flights = Flight.objects.filter(
        Q(pic=member) | Q(co=member),
        airplane__owner__in=morgs_qs,
    )

    # The manager can see all of the member's abilities.
    abilities = Ability.objects.filter(
        user=member,
    ).order_by(
        F('expires').asc(nulls_last=True),
        'kind',
    )

    # The manager can only see reservations of airplanes that he is responsible for.
    reservations = Reservation.objects.filter(
        user=member,
        airplane__owner__in=morgs_qs,
    )

    # The manager can only see the membership history of organizations that he is responsible for.
    memberships = Membership.objects.filter(
        user=member,
        orga__in=morgs_qs,
    )

    return render(request, "Organizations/member_overview.html", {
        "member": member,
        "flights": flights,
        "abilities": abilities,
        "reservations": reservations,
        "memberships": memberships,
        "organizations": None,
    })
