from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.formfields import PhoneNumberField

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
    phone = PhoneNumberField(help_text="Enter phone number with country code")
    email = models.EmailField()
    
    # MAILING ADDRESS
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    postal = models.CharField(max_length=10)
    
    
    
