from django.urls import path
from .views import flights


app_name = 'aviation'

urlpatterns = [
  # path('flights/', flights.list_view, name='flight-list'),
  # path('users/<int:user_id>/flights/', flights.list_view, name='flight-list'),
    path('flights/add/', flights.create_view, name='flight-add'),
    path('users/<int:user_id>/flights/add/', flights.create_view, name='flight-add'),
  # path('flights/<int:flight_id>/', flights.update_view, name='flight-update'),
  # path('flights/<int:flight_id>/delete/', flights.delete_view, name='flight-delete'),
]
