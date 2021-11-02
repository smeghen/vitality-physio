from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('view/', views.view_contact, name='view_contact'),
]
