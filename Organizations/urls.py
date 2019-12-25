from django.urls import path
from .views import welcome


app_name = 'organizations'

urlpatterns = [
    path('', welcome.view, name='welcome'),
]
