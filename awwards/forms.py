from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Profile
        fields = ('Email', 'user')

class ProjectUpload(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'post_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
        
