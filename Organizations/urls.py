from django.urls import path, reverse_lazy
from Accounts.views import auth
from .views import abilities, welcome, user_overview


app_name = 'organizations'

urlpatterns = [
    path('', welcome.view, name='welcome'),
    path('login/', auth.LoginView.as_view(template_name='Organizations/auth_login.html', default_next='organizations:personal-overview'), name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='Organizations/auth_logout.html'), name='logout'),
    path('password-change/', auth.PasswordChangeView.as_view(template_name='Organizations/auth_password_change.html', success_url=reverse_lazy('organizations:password-change-done')), name='password-change'),
    path('password-change-done/', auth.PasswordChangeDoneView.as_view(template_name='Organizations/auth_password_change_done.html'), name='password-change-done'),
  # path('settings/', …),   # or 'profile'?

    # Q: Why do we need all those `member/<int:user_id>/logbook/add-flight/` (a manager enters
    # a flight for someone else) and similar URLs, when a single and simple `add-flight/` might
    # suffice? After all, there is our "saving always succeeds" guarantee, where everyone can
    # enter anything.
    #
    # A: All the `…/add-flight/` URLs are needed for proper association: If there was only a
    # single `add-flight/` URL, what if the manager made a typo and we would, after the fact,
    # not be able to identify the person the flight was intended for?
    # Note that under `add-flight/`, we would not be able to *require* a known name for the
    # pilot or copilot during input validation, because we want to tolerate typos and for e.g.
    # flights for an airfield's logbook none are needed anyways.
    # It's similar for other combinations, e.g. a manager entering the flights of an airplane's
    # paper logbook: we need to make sure that the flight is associated to the intended
    # airplane, so that it may not disappear (as "detached" and therefore unreachable)
    # in the database, while still keeping our "saving always succeeds" promise.

    path('overview/', user_overview.personal_view, name='personal-overview'),
  # path('memberships/', …),    # Not useful: a user can *not* edit his own memberships.
  # path('logbook/', …),
  # path('logbook/add-flight/', …),
    path('abilities/', abilities.list_view, name='ability-list'),
    path('abilities/add/', abilities.create_view, name='ability-add'),
  # path('reservations/', …),
  # path('reservations/add/', …),

  # path('organization/<int:org_id>/', …),
  # path('organization/<int:org_id>/members/', …),
  # path('organization/<int:org_id>/members/add/', …),
  # path('organization/<int:org_id>/airplanes/', …),
  # path('organization/<int:org_id>/airplanes/add/', …),
  # path('organization/<int:org_id>/airfields/', …),
  # path('organization/<int:org_id>/airfields/add/', …),
  # path('organization/<int:org_id>/update/', …),
  # path('organization/<int:org_id>/delete/', …),   # really??

    path('member/<int:user_id>/', user_overview.member_view, name='member-overview'),
  # path('member/<int:user_id>/memberships/', …),
  # path('member/<int:user_id>/logbook/', …),
  # path('member/<int:user_id>/logbook/add-flight/', …),
    path('member/<int:user_id>/abilities/', abilities.list_view, name='ability-list'),
    path('member/<int:user_id>/abilities/add/', abilities.create_view, name='ability-add'),
  # path('member/<int:user_id>/reservations/', …),
  # path('member/<int:user_id>/reservations/add/', …),

  # path('ability/<int:ability_id>/', …),   # The list views are enough, no need for a detail view.
    path('ability/<int:ability_id>/update/', abilities.update_view, name='ability-update'),
    path('ability/<int:ability_id>/delete/', abilities.delete_view, name='ability-delete'),

  # path('airfield/<str:desig>/', …),       # Overview with map and logbook excerpt.
  # path('airfield/<str:desig>/logbook/', …),
  # path('airfield/<str:desig>/logbook/add-flight/', …),
  # path('airfield/<str:desig>/update/', …),
  # path('airfield/<str:desig>/delete/', …),

  # path('airplane/<str:callsign>/', …),    # Overview with photo and logbook excerpt.
  # path('airplane/<str:callsign>/logbook/', …),
  # path('airplane/<str:callsign>/logbook/add-flight/', …),
  # path('airplane/<str:callsign>/reservations/', …),
  # path('airplane/<str:callsign>/reservations/add/', …),
  # path('airplane/<str:callsign>/update/', …),
  # path('airplane/<str:callsign>/delete/', …),

  # path('flight/<int:flight_id>/', …),     # The list views are enough? No need for a detail view?
  # path('flight/<int:flight_id>/update/', …),
  # path('flight/<int:flight_id>/delete/', …),

  # path('reservation/<int:res_id>/', …),   # The list views are enough, no need for a detail view.
  # path('reservation/<int:res_id>/update/', …),
  # path('reservation/<int:res_id>/delete/', …),
]
