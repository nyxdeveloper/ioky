from django.shortcuts import render
from django.views import View
from .models import *


class AboutView(View):
    def get(self, request):
        team = TeamMember.objects.all()
        gallery = StoryGalleryPhoto.objects.all()
        storys = Story.objects.all()
        partners = Partner.objects.all()

        return render(request, 'about.html', {
            'team': team,
            'gallery': gallery,
            'storys': storys,
            'partners': partners
        })
