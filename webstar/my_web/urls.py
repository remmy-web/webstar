from django.urls import path
from . import views

urlpatterns=[
    path('home/', views.homepage, name='homepage'),
    path('about/', views.aboutus, name='about'),
]