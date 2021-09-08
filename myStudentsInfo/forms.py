from django import forms
from .models import User


class StudentsInformation(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'S_id':forms.TextInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'sex': forms.TextInput(attrs={'class': 'form-control'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_education': forms.TextInput(attrs={'class': 'form-control'}),

        }