from django.shortcuts import render, redirect
from .forms import CreateTaskForm, CreateCategoryForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Tasks, Category
        

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
            
            private = request.POST.get('private') 
            if private == 'true' :
                task.private = True
            task.functor = request.user
            messages.success(request, 'The task creation was successful', extra_tags='create-task')
            task.save()
            return redirect('Home')
    else:

        form = CreateTaskForm()
    context = {
        'form' : form,
        'button': 'Create',
    }
    return render(request, 'Tasks/create_task.html', context)

@login_required
def show_all_tasks_view(request):
    tasks = Tasks.objects.filter(functor = request.user)
    context = {'tasks': tasks}
    return render(request, 'Tasks/show-all-tasks.html', context)

@login_required
def delete_task_view(request, task_id):
    task = Tasks.objects.get(id=task_id)
    task.delete()
    messages.success(request, 'Task Deleted !', extra_tags='delete')
    return redirect('show-tasks')

@login_required
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
        'button': 'Update',
    }
    return render(request, 'Tasks/create_task.html', context)

@login_required
def show_categories(request):
    categories = Category.objects.filter(functor = request.user)
    print(categories)
    context = {'categories': categories}
    return render(request, 'Tasks/categories.html', context)

@login_required 
def create_category_view(request):
    if request.method == 'POST':
        form = CreateCategoryForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.functor = request.user
            messages.success(request, 'The category creation was successful', extra_tags='create-category')
            task.save()
            return redirect('categories')
    else:

        form = CreateCategoryForm()
    context = {
        'form' : form,
        'button': 'Create',
    }
    return render(request, 'Tasks/create-category.html', context)