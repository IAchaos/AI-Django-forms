from django import forms
from .models import Student

class RegistationForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = [
            "first_name",
            "last_name",
            "dob",
            "instrument",
            "days",
            "start_datetime",
            "comments"
        ]
        
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name',
            }),
            
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name',
            }),
            
            'dob': forms.SelectDateWidget(
                years=range(1950, 2025),
                empty_label='None'
            ),
            'start_datetime': forms.SplitDateTimeWidget(
                attrs={'type': 'datetime-local'},
                date_attrs={'type': 'date'},
                time_attrs={'type': 'time'}
            ),
            'days': forms.CheckboxSelectMultiple(),
            'comments': forms.Textarea(attrs={
                'Placeholder': 'If you have any remarks right down here'
            })
        }   