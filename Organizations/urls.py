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

    path('overview/', user_overview.personal_view, name='personal-overview'),
    path('member/<int:user_id>/overview/', user_overview.member_view, name='member-overview'),

    path('abilities/', abilities.list_view, name='ability-list'),
    path('users/<int:user_id>/abilities/', abilities.list_view, name='ability-list'),
    path('abilities/add/', abilities.create_view, name='ability-add'),
    path('users/<int:user_id>/abilities/add/', abilities.create_view, name='ability-add'),
    path('abilities/<int:ability_id>/', abilities.update_view, name='ability-update'),
    path('abilities/<int:ability_id>/delete/', abilities.delete_view, name='ability-delete'),
]
