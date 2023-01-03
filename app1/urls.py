from django.urls import path
from app1.views import *
app_name='amarnadh'

urlpatterns=[
    path('amar/',amar,name='amar'),
]