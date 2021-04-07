from django import forms
from .models.project import Project, Project_Pictures
from .models.comment import Comment


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

class CommentForm(forms.ModelForm):
    text = forms.CharField(label ="", widget = forms.Textarea(
    attrs ={
        'class':'form-control',
        'placeholder':'Comment here !',
        'rows':4,
        'cols':70,
    }))
    class Meta:
        model = Comment
        fields =['text',]