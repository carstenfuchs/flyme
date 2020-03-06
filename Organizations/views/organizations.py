from datetime import date, timedelta

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, render

from Aviation.models import Airfield, Airplane
from Organizations.common import get_managed_organizations
from Organizations.models import Ability, Membership


@login_required
@transaction.non_atomic_requests
def overview(request, org_id):
    morgs_qs = get_managed_organizations(request.user)
    org = get_object_or_404(morgs_qs, id=org_id)
    today = date.today()
    memberships = Membership.objects.filter(orga=org, begin__lte=today, end__gte=today).exclude(status="x")
    ex_ab = Ability.objects.filter(user__membership__in=memberships, expires__lt=today + timedelta(days=32))
    airplanes = Airplane.objects.filter(owner=org)
    airfields = Airfield.objects.filter(operator=org)

    return render(request, "Organizations/organization_overview.html", {
        "org": org,
        "memberships": memberships,
        "expiring_abilities": ex_ab,
        "airplanes": airplanes,
        "airfields": airfields,
    })
