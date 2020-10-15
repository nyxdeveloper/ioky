from django.shortcuts import render, redirect
from django.views import View
from .models import *
from .forms import *


class ForPartnersView(View):
    def get(self, request):
        info = Info.objects.last()
        documents = Document.objects.filter(public=True)
        form = PartnersForm()
        return render(request, 'for-partners.html', {
            'info': info,
            'docs': documents,
            'form': form,
        })


class AddPartner(View):
    def post(self, request):
        bound_form = PartnersForm(request.POST)
        if bound_form.is_valid():
            bound_form.save()
            return redirect('/for-partners/thanks/')
        return redirect('/')


class Thanks(View):
    def get(self, request):
        return render(request, 'thanks.html')
