from django.urls import path
from .views import RoomView
from .views import main

urlpatterns = [
    path('', main),
    path('room', RoomView.as_view()), # return main response from views
]
