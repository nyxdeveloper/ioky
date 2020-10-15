from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectsView.as_view(), name='projects'),
    path('<slug:slug>/', views.ProjectDetail.as_view(), name='project-detail')
]