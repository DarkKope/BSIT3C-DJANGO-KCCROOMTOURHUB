from django.contrib import admin
from django.urls import path, include
from apps.Tour import views as tour_views 

# Import your old views (assuming they are in mysite/views.py)
from . import views as mysite_views 

