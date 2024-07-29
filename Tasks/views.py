from django.shortcuts import render, redirect
from .forms import CreateTaskForm, CreateCategoryForm, CreateCommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Tasks, Category, Comment
from django.db.models import Q

        

@login_required
def create_task_view(request):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST, user=request.user)
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

        form = CreateTaskForm(user=request.user)
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
    if request.user != task.functor:
            messages.error(request, 'You are not allowed to delete this task', extra_tags='perm-delete')
            return redirect('public-tasks')
    task.delete()
    messages.success(request, 'Task Deleted !', extra_tags='delete')
    return redirect('show-tasks')

@login_required
def update_task_view(request, task_id):
    task = Tasks.objects.get(id=task_id)
    if request.method == 'POST':
        if request.user != task.functor:
            messages.error(request, 'You are not allowed to update this task', extra_tags='perm-update')
            return redirect('public-tasks')
        form = CreateTaskForm(request.POST, instance=task, user=request.user)
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
        form = CreateTaskForm(instance=task, user=request.user)
    context = {
        'form' : form,
        'button': 'Update',
    }
    return render(request, 'Tasks/create_task.html', context)

@login_required
def show_categories(request):

    categories = Category.objects.filter(functor = request.user)
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


@login_required
def delete_category_view(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    messages.success(request, 'Category Deleted !', extra_tags='delete-category')
    return redirect('categories')

@login_required
def update_category_view(request, category_id):

    category = Category.objects.get(id=category_id)

    if request.method == 'POST':
    
        form = CreateCategoryForm(request.POST, instance=category)
        if form.is_valid():

            form.save(commit=False)
            form.functor = request.user
            form.save()
            messages.success(request, 'The category update was successful', extra_tags='update-category') 
            return redirect('categories')       
        
    else:

        form = CreateCategoryForm(instance=category)

    context = {
        'form': form,
        'button': 'Update'
    }
    
    return render(request, 'Tasks/create-category.html', context)


@login_required
def show_task_by_category_view(request, category_id):

    tasks = Tasks.objects.filter(category__id=category_id)
    context = {'tasks': tasks}
    return render(request, 'Tasks/show-all-tasks.html', context)

@login_required
def comments_view(request, task_id):
    comments = Comment.objects.filter(task__id= task_id)
    if request.method == 'POST':
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.Author = request.user
            comment.task = Tasks.objects.get(id=task_id)
            comment.save()
            messages.success(request, 'A comment was made', extra_tags='comment')
            return redirect('comments', task_id=task_id)
    else:
        form = CreateCommentForm()
    context = {
        'comments': comments, 
        'form': form,
        'button': 'Send',
        'task_id': task_id,
        }
    return render(request, 'Tasks/comments.html', context)


@login_required
def delete_comment_view(request, task_id, comment_id):
    comment = Comment.objects.get(id= comment_id)
    if comment.Author == request.user:
        comment.delete()
        messages.success(request, 'The comment was deleted', extra_tags='delete-comment')
    else :
        messages.error(request, 'You are not allowed to delete comments', extra_tags='delete-comment')

    return redirect('comments', task_id=task_id)

def show_public_tasks_view(request):
    public_tasks = Tasks.objects.filter(private=False)
    context = {
        'tasks': public_tasks 
    }
    return render(request, 'Tasks/show-all-tasks.html', context)


def search_view(request):
    
    if request.method == 'GET':
        search_str = request.GET.get('search')
        tasks = Tasks.objects.filter(Q(name__contains=search_str, functor=request.user, private=True) | Q(private=False, name__contains=search_str))
        context = {
            'tasks': tasks
        }
        return render(request, 'Tasks/show-all-tasks.html', context)
    
    return redirect(request.META.get('HTTP_REFERER', '/'))