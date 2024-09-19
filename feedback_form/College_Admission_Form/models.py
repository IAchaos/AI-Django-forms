from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

# College Admission Form
class CollegeAdmission(models.Model):
    # NAME
    fname = models.CharField(max_length=255)
    iname = models.CharField(max_length=255)
    lname= models.CharField(max_length=255)
    
    # DOB
    dob = models.DateField(null=True, blank=True)
    # GENDER
    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        
    gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.MALE)
    
    # COUNTRY
    country = CountryField(blank_label='(Select Country)')
    # PHONE & EMAIL 
    phone = PhoneNumberField(help_text="Enter phone number with country code",default='')
    email = models.EmailField()
    
    # MAILING ADDRESS
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    postal = models.CharField(max_length=10)
    
    # CONTACT EMERGENCY
    emrg_fname= models.CharField(max_length=255, default='')
    emrg_lname = models.CharField(max_length=255, default='')
    relationship = models.CharField(max_length=100 , default='')
    emrg_email = models.EmailField(default='')
    emrg_phone = PhoneNumberField(help_text='Enter your emergancy number',default='')
    
    # SPEAKING LANGAUGES
    class Answer(models.TextChoices):
        YES = 'Y' , 'Yes'
        NO = 'N', 'No'
        
    english = models.CharField(max_length=1, choices=Answer.choices, default=Answer.NO)
    list_lang= models.TextField(max_length=500, blank=True)
    
    
    
    
    
