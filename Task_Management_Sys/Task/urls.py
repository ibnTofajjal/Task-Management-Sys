

from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_task, name="add_task"),
    path('delete/<int:id>', views.delete_task, name="delete_task"),
]
