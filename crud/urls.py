from django.urls import path
from . import views  # Import views from the current app


urlpatterns=[
    path('create/', views.create_student, name="create_student"),
    path('', views.read_students, name="read_students"),
    path('update/<str:student_id>/', views.update_student, name="update_student"),
    path('delete/<str:student_id>/', views.delete_student, name="delete_student")
]
