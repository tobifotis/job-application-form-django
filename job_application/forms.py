# Frontend form model
from django import forms

class ApplicationForm(forms.Form):
    """
    Form class to capture job application data from the frontend.
    This class handles form rendering and validation for user input.
    """
    first_name = forms.CharField(max_length=80)  # Applicant's first name
    last_name = forms.CharField(max_length=80)   # Applicant's last name
    email = forms.EmailField()                   # Applicant's email address
    date = forms.DateField()                     # Available start date
    occupation = forms.CharField(max_length=80)  # Applicant's current occupation status
