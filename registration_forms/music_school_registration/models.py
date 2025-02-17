from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Student(models.Model):
    
    # NAME
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    
    # DADE OF BIRTH
    dob = models.DateField()
    
    # CHOICE OF THE INSTRUMENT
    class Instruments(models.TextChoices):
        VIOLIN = 'VL', 'Violin'
        GUITAR = 'GT', 'Guitar'
        BASS = 'BS', 'Bass'
        DRUMS = 'DR', 'Drums'
        VOCALS = 'VC', 'Vocals'
        
    instrument = models.CharField(max_length=2, choices=Instruments.choices , default=Instruments.VIOLIN)
    
    # DAYS OF CLASSES
    class Days(models.TextChoices):
        MONDAY = 'Monday', 'Monday'
        TUESDAY = 'Tuesday', 'Tuesday'
        WEDNESDAY = 'Wednesday', 'Wednesday'
        THURSDAY = 'Thursday', 'Thursday'
        FRIDAY = 'Friday', 'Friday'
        SATURDAY = 'Saturday', 'Saturday'
        SUNDAY = 'Sunday', 'Sunday'
    
    
    days = models.JSONField(default=list)
    
    # START DATE & TIME
    start_datetime = models.DateTimeField()
    
    # Comments
    comments = models.TextField(blank=True )
    

        

    class Meta:
        verbose_name = _("Student")
        verbose_name_plural = _("Students")

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("Student_detail", kwargs={"pk": self.pk})

