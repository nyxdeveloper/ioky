from django import forms
from .models import *


class QuestionForm(forms.Form):
    name = forms.CharField(max_length=100, label='Имя', required=False)
    Email = forms.EmailField(label='Почта', required=False)
    question = forms.CharField(widget=forms.Textarea, label='Вопрос')

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'height': '3vh'})
        self.fields['Email'].widget.attrs.update({'class': 'form-control', 'height': '3vh'})
        self.fields['question'].widget.attrs.update({'class': 'form-control'})

    def save(self):
        new_question = Question.objects.create(
            name=self.cleaned_data['name'],
            Email=self.cleaned_data['Email'],
            question=self.cleaned_data['question']
        )
        return new_question
