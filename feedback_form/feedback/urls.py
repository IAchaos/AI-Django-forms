from django.urls import path
from . import views

app_name= 'feedback'
urlpatterns = [
    path('home', views.feedbackHandler, name='home'),
    path('message', views.messages, name='message')
]
