from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy


app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='Accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Accounts/logout.html'), name='logout'),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='Accounts/password_change.html', success_url=reverse_lazy('accounts:password-change-done')), name='password-change'),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(template_name='Accounts/password_change_done.html'), name='password-change-done'),
]
