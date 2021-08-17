from django.forms import ModelForm
from django.urls import reverse_lazy

from projectapp.models import Project


class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'image', 'description']
