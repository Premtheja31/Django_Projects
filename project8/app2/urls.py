from django.urls import path
from app2.views import *
app_name='mine'
urlpatterns=[
    path('hello/',hello,name='hello'),
]