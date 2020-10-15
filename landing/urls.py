from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('create-question/', views.CreateQuestion.as_view(), name='create-question')
]