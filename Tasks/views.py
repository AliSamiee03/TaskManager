from django.shortcuts import render, redirect
from .forms import CreateTaskForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Tasks
        

@login_required
def create_task_view(request):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            if task.start_date > task.end_date :
                messages.error(request, 'The start time must be before the end time', extra_tags='time-input-error')
                return redirect('create-task')

            if 0 > task.progress or task.progress > 100 :
                messages.error(request, 'Progress should be between 0 and 100', extra_tags='progress-error')
                return redirect('create-task')   
            
            task.functor = request.user
            messages.success(request, 'The task creation was successful', extra_tags='create-task')
            task.save()
            return redirect('Home')
    else:

        form = CreateTaskForm()
    context = {
        'form' : form,
    }
    return render(request, 'Tasks/create_task.html', context)

def show_all_tasks_view(request):
    tasks = Tasks.objects.all()
    context = {'tasks': tasks}
    return render(request, 'Tasks/show-all-tasks.html', context)

def delete_task_view(request, task_id):
    task = Tasks.objects.get(id=task_id)
    task.delete()
    messages.success(request, 'Task Deleted !', extra_tags='delete')
    return redirect('show-tasks')

def update_task_view(request, task_id):
    task = Tasks.objects.get(id=task_id)
    if request.method == 'POST':
        form = CreateTaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            if task.start_date > task.end_date :
                messages.error(request, 'The start time must be before the end time', extra_tags='time-input-error')
                return redirect('update-task', task_id=task_id)

            if 0 > task.progress or task.progress > 100 :
                messages.error(request, 'Progress should be between 0 and 100', extra_tags='progress-error')
                return redirect('update-task', task_id=task_id)   
            
            task.functor = request.user
            messages.success(request, 'The task update was successful', extra_tags='update-task')
            task.save()
            return redirect('show-tasks')
    else:

        form = CreateTaskForm(instance=task)
    context = {
        'form' : form,
    }
    return render(request, 'Tasks/create_task.html', context)