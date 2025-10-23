from django.urls import path
from . import views

urlpatterns = [
    path('slots/', views.view_slots, name='view_slots'),
    path('book/<int:slot_id>/', views.book_slot, name='book_slot'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),

    path('location/', views.location_view, name='location'),
]
