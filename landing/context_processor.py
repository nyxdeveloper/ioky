from landing.models import *
from .forms import QuestionForm
from forPartners.models import *
from projects.models import *
from about.models import *


def question(request):
    return {
        'questions': Question.objects.all(),
        'questionForm': QuestionForm()
    }


def landing(request):
    return {
        'documents': Info.objects.last(),
        'projects': Project.objects.all(),
    }


def documents(request):
    return {
        'documents': Document.objects.filter(public=True)
    }
