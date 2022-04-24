from django.urls import path
from . import views

urlpatterns = [
    path('', views.students_list, name='students-list'),
    path('create/', views.create_student, name='create-student'),
    path('edit/<str:pk>/', views.edit_student, name='edit-student'),
    path('delete/<str:pk>/', views.delete_student, name='delete-student'),
]