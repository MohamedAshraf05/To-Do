from django.urls import path
from .views import get_tasks , get_specific_object , delete_task , add_tasks , update_task , RegisterView
from django.contrib.auth.views import LoginView , LogoutView
urlpatterns = [
    path("all-tasks/" ,get_tasks.as_view() , name="task-list"),
    path("add-tasks/" , add_tasks.as_view(), name="add-task"),
    path("update-task/<int:pk>/" , update_task.as_view(), name="update-task"),
    path("task/<int:pk>/" , get_specific_object.as_view() , name="get-specific-object"),
    path("delete/<int:pk>/" , delete_task.as_view() , name="delete"),
    path("register/" , RegisterView.as_view() , name="register"),
    path("login/" , LoginView.as_view(
        template_name="tasks/login.html",
        redirect_authenticated_user = True
    ) , name="login"),
    path("logout/" , LogoutView.as_view() , name="logout")
]

# Primary key -> id + unique 