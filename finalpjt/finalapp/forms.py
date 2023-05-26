from django import forms
from django.db import models

class RegistrationForm(forms.Form):
      name = forms.CharField()
      dob = forms.DateField()
      age = forms.IntegerField()
      gender = forms.ChoiceField(choices=[('male','Male'), ('female','Female'), ('transgender','Transgender')])
      phone_number = forms.CharField()
      email = forms.EmailField()
      password = forms.CharField(widget=forms.PasswordInput)
      address = forms.CharField(widget=forms.Textarea)
      district = forms.ChoiceField(choices=[('calicut', 'Calicut'), ('cochin', 'Cochin'), ('kollam', 'Kollam'), ('kottayam', 'Kottayam'),('malappuram','Malappuram'),('palakad','Palakkad')])
      branches = forms.ChoiceField(choices=([]))
      account_type = forms.ChoiceField(choices=[('savings', 'Savings'), ('current', 'Current')])
      materials_required = forms.MultipleChoiceField(choices=[('debit', 'Debit Card'), ('credit', 'Credit Card'), ('cheque', 'Chequebook')], widget=forms.CheckboxSelectMultiple)
