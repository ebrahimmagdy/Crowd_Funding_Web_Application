from django import forms
from .models.project import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'details', 'total_target', 'start_date', 'end_date', 'category']
        labels = {
            'title': 'Project Title',
            'details': 'Project Details',
            'total_target': 'Total Target',
            'start_date': 'Start Date',
            'end_date': 'End Date',
            'category': 'Category'
        }
