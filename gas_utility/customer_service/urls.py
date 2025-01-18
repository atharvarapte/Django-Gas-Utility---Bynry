from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_request, name='create_request'),
    path('track/', views.track_request, name='track_request'),
    path('details/<int:request_id>/', views.request_details, name='request_details'),
]
