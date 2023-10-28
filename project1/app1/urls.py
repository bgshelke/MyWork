from django.urls import path
from .views import *

urlpatterns =[
    path('ev/',enquiry_view,name='enquiry_url'),
    path('sv/',display_view,name='show_url'),
    path('cv/',contact_view,name='contact_url')
]