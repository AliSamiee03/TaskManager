from django import forms
from .models import Tasks, Category, Comment

class CreateTaskForm(forms.ModelForm):
    class Meta: 
        model = Tasks
        fields = ['name', 'start_date', 'end_date', 'progress', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateTimeInput(attrs={'class': 'create-input', 'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'class': 'create-input', 'type': 'datetime-local'}),
            'progress': forms.NumberInput(attrs={'class': 'create-input'}),
            'category': forms.Select(attrs={'class': 'create-input', 'id': 'category-input'}),
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(functor=user)

class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['description']
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'})
        }
