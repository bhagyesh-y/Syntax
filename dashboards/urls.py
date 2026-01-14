from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    # Category CRUD Operations
    path('categories/',views.categories,name='categories'),
    path('category/add/',views.add_category,name='add_category'),
    path('category/edit/<int:pk>/',views.edit_category,name='edit_category'),
    path('category/delete/<int:pk>/',views.delete_category,name='delete_category'),
    # Blog Posts CRUD
    path('posts/', views.posts,name='posts'),
    path('posts/add/',views.add_post,name='add_post'),
]

