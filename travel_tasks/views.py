from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from .models import TravelTask
from .forms import TravelTaskForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import AccessMixin


class CustomLoginRequiredMixin(LoginRequiredMixin, AccessMixin):
    """ Custom mixin to add a message when user is not logged in. """

    def handle_no_permission(self):
        messages.error(
            self.request, "You are not logged in. Please log in to continue.")
        return redirect('account_login')


class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'travel_tasks/home.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # Redirect to task list if user is authenticated
            return redirect('task_list')
        return super().get(request, *args, **kwargs)


class TaskListView(CustomLoginRequiredMixin, ListView):
    """
    Displays a list of tasks for the logged-in user
    """
    model = TravelTask
    template_name = 'travel_tasks/task_list.html' 
    context_object_name = 'tasks'

    def get_queryset(self):
        # Filter tasks to only include those created by the logged-in user
        return TravelTask.objects.filter(user=self.request.user)


class TaskCreateView(CustomLoginRequiredMixin, CreateView):
    """
    Allows the user to create a new task
    """
    model = TravelTask
    form_class = TravelTaskForm
    template_name = 'travel_tasks/task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Task created successfully!')
        return super().form_valid(form)


class TaskDetailView(CustomLoginRequiredMixin, DetailView):
    """
    Displays details of a specific task
    """
    model = TravelTask
    template_name = 'travel_tasks/task_detail.html' 
    context_object_name = 'task'


class TaskUpdateView(CustomLoginRequiredMixin, UpdateView):
    """
    Allows the user to update an existing task
    """
    model = TravelTask
    form_class = TravelTaskForm
    template_name = 'travel_tasks/task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        messages.success(self.request, 'Task updated successfully!')
        return super().form_valid(form)


class TaskDeleteView(CustomLoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """
    Allows the user to delete a task
    """
    model = TravelTask
    template_name = 'travel_tasks/task_delete.html'
    success_url = reverse_lazy('travel_tasks/task_list')
    success_message = "Task deleted successfully!"

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, self.success_message)
        return response


class TaskCancelView(CustomLoginRequiredMixin, View):
    """
    Allows the user to cancel a task (sets status to 'Cancelled')
    """
    def post(self, request, pk, *args, **kwargs):
        task = get_object_or_404(TravelTask, pk=pk)
        task.status = 'Cancelled'
        task.save()
        messages.success(request, 'Task cancelled successfully!')
        return redirect('task_list')

