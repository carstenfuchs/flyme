from django.urls import path, reverse_lazy
from Accounts.views import auth
from .views import welcome, user_overview


app_name = 'organizations'

urlpatterns = [
    path('', welcome.view, name='welcome'),
    path('login/', auth.LoginView.as_view(template_name='Organizations/auth_login.html', default_next='organizations:user-overview'), name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='Organizations/auth_logout.html'), name='logout'),
    path('password-change/', auth.PasswordChangeView.as_view(template_name='Organizations/auth_password_change.html', success_url=reverse_lazy('organizations:password-change-done')), name='password-change'),
    path('password-change-done/', auth.PasswordChangeDoneView.as_view(template_name='Organizations/auth_password_change_done.html'), name='password-change-done'),
    path('overview/', user_overview.view, name='user-overview'),
    path('users/<int:user_id>/overview/', user_overview.view, name='user-overview'),
]
