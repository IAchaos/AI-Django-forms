from django import forms
from .models import CollegeAdmission
from phonenumber_field.formfields import PhoneNumberField  # Ensure correct import

# Admission Form Creation
class CollegeAdmissionForm(forms.ModelForm):
    
    class Meta:
        model = CollegeAdmission
        fields = ['fname', 'iname', 'lname', 'dob', 'gender', 'country', 'phone', 'email', 
                  'street_address', 'city', 'province', 'postal', 
                  'emrg_fname', 'emrg_lname', 'relationship', 'emrg_email', 'emrg_phone', 
                  'english', 'list_lang']

        widgets = {
            'fname': forms.TextInput(attrs={'placeholder':'First Name'}),
            'lname': forms.TextInput(attrs={'placeholder':'Last Name'}),
            'iname': forms.TextInput(attrs={'placeholder':'Intial Name'}),
            'dob': forms.SelectDateWidget(years=range(1950, 2025)),  # Date of birth
        }
        
        labels = {
            'fname': 'First Name',
            'iname': 'Intial Name',
            'lname': 'Last Name'
        }
