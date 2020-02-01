from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.views.generic import ListView

from Organizations.common import get_relevant_user_or_404
from Organizations.models import Ability

# TODO?
# @transaction.non_atomic_requests


class AbilityList(LoginRequiredMixin, ListView):
    # model = Ability
    # template_name = "Organizations/ability_list.html"
    # context_object_name = "ability_list"

    def get_queryset(self):
        self.u = get_relevant_user_or_404(self.request, self.kwargs.get('user_id'))
        return Ability.objects.filter(user=self.u).order_by(F('expires').asc(nulls_last=True), 'kind')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['u'] = self.u
        return context
