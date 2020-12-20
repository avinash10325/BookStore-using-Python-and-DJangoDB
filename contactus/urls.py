from django.urls import path
from .views import *

urlpatterns = [
    path('contactus', contactus , name='contactus'),

]