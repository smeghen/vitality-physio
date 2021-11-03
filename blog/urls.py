from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('blog/', views.add_blog, name='add_blog'),
]
