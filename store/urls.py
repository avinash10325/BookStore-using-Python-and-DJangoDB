from django.urls import path
from .views import *

urlpatterns = [
    path('store', store , name='store'),
    path(r'^purchase/(?P<id>\d+)/$', purchase , name='purchase'),
]