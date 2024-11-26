from django import forms
from.models import user 

class student(forms.ModelForm):
    class Meta:
        model=user
        fields=['username','email','password']