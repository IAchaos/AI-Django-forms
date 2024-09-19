from django.urls import path
from . import views

app_name = 'college-admission'

urlpatterns = [
    path('home', views.collegeAdmission, name='college-adm' ),
]
