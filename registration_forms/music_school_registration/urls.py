from django.urls import path
from .import views

app_name = 'music-school-registration'

urlpatterns = [
    path("", views.registration, name="registration_form")
]
