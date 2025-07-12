# Database model
from django.db import models

class Form(models.Model):
    """
    Model representing a job application submission.
    Stores applicant's personal and employment-related details.
    """
    first_name = models.CharField(max_length=80)  # First name of the applicant
    last_name = models.CharField(max_length=80)   # Last name of the applicant
    email = models.EmailField()                   # Email address of the applicant
    date = models.DateField()                     # Date the applicant is available to start
    occupation = models.CharField(max_length=80)  # Current occupation of the applicant

    def __str__(self):
        """
        Returns a readable string representation of the applicant.
        """
        return f"{self.first_name} {self.last_name}"
