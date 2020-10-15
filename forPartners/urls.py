from django.urls import path
from . import views

urlpatterns = [
    path('', views.ForPartnersView.as_view(), name='for-partners'),
    path('add-partner/', views.AddPartner.as_view(), name='add-partner'),
    path('thanks/', views.Thanks.as_view(), name='thanks')
]