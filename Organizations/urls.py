from django.urls import path
from django.contrib.auth import views as auth_views
from Accounts.views import auth
from .views import welcome, user_overview


app_name = 'organizations'

urlpatterns = [
    path('login/', auth.LoginView.as_view(template_name='Organizations/auth_login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Organizations/auth_logout.html'), name='logout'),
    path('password-change/', auth.PasswordChangeView.as_view(template_name='Organizations/auth_password_change.html'), name='password-change'),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(template_name='Organizations/auth_password_change_done.html'), name='password-change-done'),
    path('', welcome.view, name='welcome'),
    path('user/overview/', user_overview.view, name='user-overview'),
]
