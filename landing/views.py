from django.shortcuts import render, redirect
from django.views import View
from .forms import *


class HomePageView(View):
    def get(self, request):
        return render(request, 'homepage.html')


class CreateQuestion(View):
    def post(self, request):
        boundForm = QuestionForm(request.POST)
        if boundForm.is_valid():
            boundForm.save()
            return redirect('/')
        return redirect('/')