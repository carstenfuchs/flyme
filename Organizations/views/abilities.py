from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import F
from django.shortcuts import get_object_or_404, redirect, render

from Organizations.common import get_managed_user, confirm_management_allowed
from Organizations.models import Ability


class AbilityForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    class Meta:
        model = Ability
        fields = ['kind', 'number', 'expires', 'remark']


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


@login_required
def create_view(request, user_id=None):
    mu = get_managed_user(request.user, user_id)

    if request.method == 'POST':
        form = AbilityForm(request.POST)

        if form.is_valid():
            ab = form.save(commit=False)
            ab.user = mu
            ab.save()
            messages.success(request, f"The ability has been created:<br>{ab}.")
            return redirect('organizations:ability-list', user_id=ab.user.id)
    else:
        form = AbilityForm()

    return render(
        request,
        'Organizations/generic_form_page.html',
        {
            'form': form,
            'title': 'Create ability',
            'submit_button_label': 'Create',
        }
    )


@login_required
def update_view(request, ability_id):
    ab = get_object_or_404(Ability, id=ability_id)
    confirm_management_allowed(request.user, ab.user)

    if request.method == 'POST':
        form = AbilityForm(request.POST, instance=ab)

        if form.is_valid():
            form.save()
            messages.success(request, f"The ability has been updated:<br>{ab}.")
            return redirect('organizations:ability-list', user_id=ab.user.id)
    else:
        form = AbilityForm(instance=ab)

    return render(
        request,
        'Organizations/generic_form_page.html',
        {
            'form': form,
            'title': 'Update ability',
            'submit_button_label': 'Update',
        }
    )


@login_required
def delete_view(request, ability_id):
    ab = get_object_or_404(Ability, id=ability_id)
    confirm_management_allowed(request.user, ab.user)

    if request.method == 'POST':
        ab.delete()
        messages.success(request, f"The ability has been deleted:<br>{ab}.")
        return redirect('organizations:ability-list', user_id=ab.user.id)

    return render(
        request,
        'Organizations/generic_form_page.html',
        {
            'title': 'Delete ability',
            'outer_lead_text': 'Do you really want to delete this ability?',
            'inner_lead_text': str(ab),
            'submit_button_label': 'Delete',
            'submit_button_class': 'btn-danger',
        }
    )
