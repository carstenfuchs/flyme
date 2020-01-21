from django.shortcuts import get_object_or_404
from Accounts.models import User


def get_relevant_user_or_404(request, user_id):
    if user_id is None or user_id == request.user.id:
        return request.user

    # TODO: Is request.user allowed to access the user with `user_id`?

    return get_object_or_404(User, id=user_id)
