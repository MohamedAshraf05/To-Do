from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import Task
from django.views.generic import ListView , CreateView , UpdateView , DetailView , DeleteView
from django.views import View 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
# Create your views here.

# authentications -> Login , Logout , Registration

# post , get 
class RegisterView(View):

    def get(self , request):
        return render(request , "tasks/register.html")
    
    def post(self , request):
        person_username = request.POST.get("username")
        person_email = request.POST.get("email")
        person_password = request.POST.get("password")

        # Check 
        if User.objects.filter(username=person_username).exists():
            messages.error(request , "Username already exists")
            return redirect("register")

        User.objects.create_user(
            username=person_username,
            email=person_email,
            password= person_password
        )        

        return redirect("login")


class get_tasks(LoginRequiredMixin,ListView):
    login_url = "login"
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "task_list"

class add_tasks(LoginRequiredMixin , CreateView):
    login_url = "login"
    model = Task
    template_name = "tasks/add_task.html"
    fields = ["title"]
    success_url = reverse_lazy("task-list")

class update_task(LoginRequiredMixin , UpdateView):
    login_url = "login"
    model = Task
    template_name = "tasks/task_list.html"
    fields = []  # no form fields
    success_url = reverse_lazy("task-list")
    
    def post(self, request, *args, **kwargs):
        task = self.get_object() 
        task.completed = not task.completed    # toggle value not true = false , not false  = true
        task.save()
        return redirect(self.success_url)



class get_specific_object( LoginRequiredMixin , DetailView):
    login_url = "login"
    model = Task
    template_name = "tasks/specific_task.html"
    context_object_name = "task"
    
    
class delete_task(LoginRequiredMixin , DeleteView):
    login_url = "login"
    model = Task
    template_name = "tasks/task_list.html"
    success_url = reverse_lazy("task-list")
