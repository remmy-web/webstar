from django.urls import path
from . import views

urlpatterns=[
    path('home/', views.homepage, name='homepage'),
    path('about/', views.aboutus, name='about'),
    path('product/', views.product, name='product'),
    path('view/', views.product_view, name='product_view'),
]