from django import forms
from .models import Emp

class ContactForm(forms.Form):
    name=forms.CharField(label="Enter your name", max_length=100)
    email=forms.EmailField(label="Enter your Email", max_length=100)
    message=forms.CharField(label="Message", widget=forms.Textarea)


    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
