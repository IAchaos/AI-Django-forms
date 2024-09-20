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
            'fname': forms.TextInput(attrs={'placeholder':'First Name',
                                            'class':'form-control'
                                            }),
            
            'lname': forms.TextInput(attrs={'placeholder':'Last Name',
                                            'class':'form-control'
                                            }),
            
            'iname': forms.TextInput(attrs={'placeholder':'Intial Name',
                                            'class':'form-control'
                                            }),
            
           'dob': forms.SelectDateWidget(
                years=range(1950, 2025),
                attrs={'class': 'form-select mb-3'}, # Adding Bootstrap class 'form-select'
                empty_label='None' 
            ),
           
           'gender': forms.RadioSelect(attrs={'class':'form-control'}),
           'country': forms.Select(attrs={'class':'form-control'}),
           
           'phone': forms.NumberInput(attrs={'class': 'form-control',
                                             'placeholder':'Enter Your Number'
                                             }),
           
           'email': forms.EmailInput(attrs={'placeholder':'ex: myname@example.com',
                                            'class':'form-control'
                                            }),
           
           'street_address': forms.TextInput(attrs={'placeholder':'Enter Yout Street Address Here ',
                                                    'class':'form-control'
                                                    }),
           
           'city': forms.TextInput(attrs={'placeholder':'Enter Your City',
                                          'class': 'form-control'
                                          }),
           
           'province': forms.TextInput(attrs={'placeholder':'Enter Province You Live At here',
                                              'class': 'form-control'
                                              }),
           
           'postal': forms.TextInput(attrs={'placeholder': 'Postal/ZIP Code',
                                            'class': 'form-control'
                                            }),
           
           'emrg_fname': forms.TextInput(attrs={'placeholder': 'First Name',
                                                'class': 'form-control'
                                                }),
           
           'emrg_lname': forms.TextInput(attrs={'placeholder': 'Last Name',
                                                'class': 'form-control'
                                                }),
           
           'emrg_email': forms.EmailInput(attrs={'placeholder':'Emergenct Email',
                                                 'class': 'form-control'
                                                 }),
           
           'emrg_phone': forms.NumberInput(attrs={'placeholder': 'Enter Emeregency Phobe Number',
                                                  'class':'form-control'
                                                  }),
           
           'relationship': forms.TextInput(attrs={'placeholder':'Who is applying this emergency',
                                                 'class': 'form-control'}),
           
            'english': forms.RadioSelect(attrs={'class':'form-control'}),

        }
        
        labels = {
            'fname': 'First Name',
            'iname': 'Intial Name',
            'lname': 'Last Name',
            'gender': 'Gender'
        }
