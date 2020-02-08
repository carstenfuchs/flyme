from django.shortcuts import get_object_or_404
from Accounts.models import User


def get_managed_user(managing_user, other_user_id):
    if other_user_id is None or other_user_id == managing_user.id:
        return managing_user

    # TODO: Is request.user allowed to access the user with `user_id`?

    return get_object_or_404(User, id=other_user_id)
