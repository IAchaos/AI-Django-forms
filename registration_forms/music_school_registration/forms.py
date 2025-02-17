from django import forms
from .models import Student

class RegistationForm(forms.ModelForm):
    
    # Override the days field to properly handle multiple selections
    days = forms.MultipleChoiceField(
        choices=Student.Days.choices,
        widget=forms.CheckboxSelectMultiple(),
        required=True
    )
    
    # Override the datetime field to properly handle split input
    start_datetime = forms.SplitDateTimeField(
        widget=forms.SplitDateTimeWidget(
            date_attrs={'type': 'date'},
            time_attrs={'type': 'time'}
        ),
    )
    
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
            'comments': forms.Textarea(attrs={
                'Placeholder': 'If you have any remarks right down here'
            })
        } 
        
        def save(self, commit=True):
            instance = super().save(commit=False)
            # Convert the days selection to a list before saving
            instance.days = list(self.cleaned_data['days'])
            if commit:
                instance.save()
            return instance