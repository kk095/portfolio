from django import forms
from .models import Contact


class Contact_form(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','email','message']
        widgets={'name':forms.TextInput(attrs={'placeholder':'Enter your name','class':'input'}),'email':forms.EmailInput(attrs={'placeholder':'Enter your email','class':'input'}),'message': forms.Textarea(attrs={'placeholder':'Write your message....','class':'input texteria'})}