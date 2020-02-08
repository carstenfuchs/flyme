from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import F
from django.shortcuts import render

from Organizations.common import get_managed_user
from Organizations.models import Ability


@login_required
@transaction.non_atomic_requests
def list_view(request, user_id=None):
    mu = get_managed_user(request.user, user_id)
    abilities = Ability.objects.filter(user=mu).order_by(F('expires').asc(nulls_last=True), 'kind')

    return render(
        request,
        'Organizations/ability_list.html',
        {'mu': mu, 'ability_list': abilities}
    )
