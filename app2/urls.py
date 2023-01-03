from django.urls import path
from app2.views import *
app_name='sri'

urlpatterns=[
    path('joshna/',joshna,name='joshna'),
]