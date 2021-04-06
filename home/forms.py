from django import forms
from .models.project import Project, Project_Pictures


class DateInput(forms.DateInput):
    input_type = 'date'

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'details', 'total_target', 'start_date', 'end_date', 'category', 'tags',]
        labels = {
            'title': 'Project Title',
            'details': 'Project Details',
            'total_target': 'Total Target',
            'start_date': 'Start Date',
            'end_date': 'End Date',
            'category': 'Category',
            'tags': 'Tags',
        }
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
        }

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')    
    class Meta:
        model = Project_Pictures
        fields = ('picture', )