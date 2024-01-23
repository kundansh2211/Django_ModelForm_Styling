from django.urls import path
from .views import student_view, display_view

urlpatterns = [
    path('', student_view),
    path('dv/', display_view),
]