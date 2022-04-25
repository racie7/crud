from django import forms
from django.forms import ModelForm
from .models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        
        fields = ('stud_name', 'stud_email', 'stud_contact', 'stud_course', 'stud_stud_id', 'image')

        widgets = {
            'stud_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'stud_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'stud_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone No.(In this format 254712313012)'}),
            'stud_course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Course'}),
            'stud_stud_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Student ID'}),
        }