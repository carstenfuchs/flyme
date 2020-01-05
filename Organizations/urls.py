from django.urls import path
from .views import welcome, user_overview


app_name = 'organizations'

urlpatterns = [
    path('', welcome.view, name='welcome'),
    path('user/overview/', user_overview.view, name='user-overview'),
]
