from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import F
from django.shortcuts import render

from Organizations.common import get_relevant_user_or_404
from Organizations.models import Ability


@login_required
@transaction.non_atomic_requests
def list_view(request, user_id=None):
    rel_user = get_relevant_user_or_404(request, user_id)
    abilities = Ability.objects.filter(user=rel_user).order_by(F('expires').asc(nulls_last=True), 'kind')

    return render(
        request,
        'Organizations/ability_list.html',
        {'u': rel_user, 'ability_list': abilities}
    )
