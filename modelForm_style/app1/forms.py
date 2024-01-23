from .models import Student
from django import forms

g_ch = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'roll': 'Roll Number',
            'name': 'Full Name',
            'dob': 'Date of Birth',
            'c_pass': 'Confirm password',
        }
        help_texts = {
            'password': '(Your password should contain 8-20 characters)',
            'c_pass': '(password and Confirm password should be same.)'
        }
        widgets = {
            'roll': forms.TextInput(
                attrs={"placeholder": 'e.g.101', "class": 'form-control'}),
            'name': forms.TextInput(
                attrs={"class": 'form-control'}),
            'dob': forms.DateInput(
                attrs={"type": 'date', "class": 'form-control'}),
            'password': forms.PasswordInput(
                attrs={"class": 'form-control'}),
            'c_pass': forms.PasswordInput(
                attrs={"class": 'form-control'}),
            'email': forms.EmailInput(
                attrs={"class": 'form-control'}),
            'gender': forms.RadioSelect(choices=g_ch),
            'address': forms.Textarea(
                attrs={"class": 'form-control', "rows": 4}),
        }

