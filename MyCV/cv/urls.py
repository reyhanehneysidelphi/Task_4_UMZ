from django.urls import path
from cv import views

urlpatterns = [
    path('', views.members, name='members'),
    path('details/<int:id>', views.details, name='details')
]

