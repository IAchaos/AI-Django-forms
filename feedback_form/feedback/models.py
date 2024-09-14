from django.db import models


# Feedback model
class FeedBackModel(models.Model):
    
    # inner class to define choices
    class Satisfaction(models.TextChoices):
        VERY_SATISFIED = 'VS', 'Very Satisified'
        SATISFIED = 'V', 'Satisfied'
        NEUTRAL = 'N', 'Neutral'
        UNSITISFIED = 'U', 'Unsitisfied'
        VERY_UNSITISFIED = 'UV', 'Very Unsitisfied'
    
    class firstUse(models.TextChoices):
        YES = 'yes', 'Yes'
        NO = 'no', 'No'
    
    
    first_use = models.CharField(default=firstUse.NO ,choices=firstUse.choices, max_length=3)
    ppl_recomd = models.CharField(default=firstUse.NO ,choices=firstUse.choices, max_length=3)
    suggestions = models.TextField(max_length=500)
    satisfaction = models.CharField(
                    max_length = 2,
                    choices = Satisfaction.choices,
                    default = Satisfaction.NEUTRAL
        )
    
    name = models.CharField(max_length=255)
    email = models.EmailField()
    reviewed = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.name + " " + self.reviewed
    
    
    
