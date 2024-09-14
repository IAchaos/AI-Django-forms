from django import forms
from .models import FeedBackModel

# Feedback form feelds

class FeedbackForm(forms.ModelForm):
    
    class Meta:
        model = FeedBackModel
        fields = ['first_use','ppl_recomd','suggestions','satisfaction', 'name','email']
        widgets = {
            'ppl_recomd': forms.RadioSelect(),
            'satisfaction': forms.RadioSelect(),
            'name': forms.TextInput(attrs={'placeholder': 'Enter you name.'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter you e-mail.'})
        }
        
       
        
        
        
