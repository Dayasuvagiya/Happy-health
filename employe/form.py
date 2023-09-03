from django import forms
from .models import Emp
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
)

class ContactForm(forms.Form):
    name=forms.CharField(label="Enter your name", max_length=100)
    email=forms.EmailField(label="Enter your Email", max_length=100)
    message=forms.CharField(label="Message", widget=forms.Textarea)


    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
