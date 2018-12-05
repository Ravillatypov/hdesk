from contact.models import Person, Company, Phone
from django import forms

class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ('',)