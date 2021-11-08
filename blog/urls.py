from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('blog/', views.add_blog, name='add_blog'),
    path('edit/<int:blog_id>/', views.edit_blog, name='edit_blog'),
]
