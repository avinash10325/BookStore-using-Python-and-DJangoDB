from django.urls import path
from .views import *

urlpatterns = [
    path('cart', cart , name='cart'),
    path(r'^remove/(?P<order_id>\d+)/$', remove , name='remove'),
    path('confirm', confirm, name='confirm'),
]