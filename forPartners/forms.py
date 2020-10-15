from django import forms
from .models import *


class PartnersForm(forms.Form):
    firstName = forms.CharField(max_length=50, label='Имя')
    lastName = forms.CharField(max_length=50, label='Фамилия', required=False)
    companyName = forms.CharField(max_length=150, label='Название организации')
    Email = forms.EmailField(label='Email')
    message = forms.CharField(max_length=1000, label='Сообщение', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(PartnersForm, self).__init__(*args, **kwargs)
        self.fields['firstName'].widget.attrs.update({'class': 'form-control m-1', 'height': '3vh'})
        self.fields['lastName'].widget.attrs.update({'class': 'form-control m-1', 'height': '3vh'})
        self.fields['companyName'].widget.attrs.update({'class': 'form-control m-1', 'height': '3vh'})
        self.fields['Email'].widget.attrs.update({'class': 'form-control m-1', 'height': '3vh'})
        self.fields['message'].widget.attrs.update({'class': 'form-control m-1'})

    def save(self):
        new_Partner = Partner.objects.create(
            firstName=self.cleaned_data['firstName'],
            lastName=self.cleaned_data['lastName'],
            companyName=self.cleaned_data['companyName'],
            Email=self.cleaned_data['Email'],
            message=self.cleaned_data['message']
        )
        return new_Partner
