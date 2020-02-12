from django.core.exceptions import PermissionDenied
from Accounts.models import User


def get_all_managed_users_QS(managing_user):
    """
    Returns a QuerySet of all users that the given user can manage (possibly
    not including himself).
    """

    # Below we would like to write
    #     membership__orga__membership__status__ne="x",
    # but it is still unclear if this is equivalent to
    #     ~Q(membership__orga__membership__status="x"),
    # Comparing the generated SQL might suffice to settle this?
    # See:
    #   - https://code.djangoproject.com/ticket/5763#comment:14
    #   - https://groups.google.com/d/msg/django-developers/T8XhqQmFrig/dxb2vjuchlQJ

    return User.objects.filter(
        membership__orga__membership__user=managing_user,
        membership__orga__membership__begin__lte=heute,
        membership__orga__membership__ende__gte=heute,
        membership__orga__membership__status__in=["a", "p", "e", "o"],  # see comment above
        membership__orga__membership__is_manager=True,
    )


def get_managed_user(managing_user, other_user_id):
    """
    If `managing_user` is permitted to manage the user with `other_user_id`,
    the related user instance is returned. Raises `PermissionDenied` otherwise.
    """
    if other_user_id is None or other_user_id == managing_user.id:
        return managing_user

    # Is `managing_user` allowed to access the user with `other_user_id`?
    # Yes, if he today has an active membership with management permission
    # in an organization in which the other user is a member as well.
    # Note that access is *not* allowed in this situation:
    #
    # managing_user --- managing member -- orga 1  (other user is not a member)
    #                \
    #                 -- non-managing member -- orga 2 -- other user is a member
    #
    try:
        return get_all_managed_users_QS(managing_user).get(id=other_user_id)
    except User.DoesNotExist:
        raise PermissionDenied


def is_management_allowed(managing_user, other_user):
    if managing_user == other_user:
        return True

    return get_all_managed_users_QS(managing_user).filter(id=other_user.id).exists()


def confirm_management_allowed(managing_user, other_user):
    """
    Makes sure that the first user is actually permitted to manage the second
    user. Raises `PermissionDenied` otherwise.
    """
    if not is_management_allowed(managing_user, other_user):
        raise PermissionDenied
