from django.urls import path
from .views import *

urlpatterns = [
    path('adminpannel', adminpannel , name='adminpannel'),
    path(r'^removeBook/(?P<book_id>\d+)/$', remove , name='removeBook'),
    path('adminlogin', adminlogin , name='adminlogin'),
    path('adminlogout', adminlogout , name='adminlogout'),
]