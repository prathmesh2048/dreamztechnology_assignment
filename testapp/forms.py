from .models import Student
from django import forms
from django.forms import widgets


class studentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            'student_dob': widgets.DateInput(attrs={'type': 'date'}),
            'student_doj': widgets.DateInput(attrs={'type': 'date'})
        }