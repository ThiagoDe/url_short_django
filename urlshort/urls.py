from django.urls import path
from .views import home, createShortURL, redirect, reverseURL

urlpatterns = [
    path('', home, name='home'),
    path('create/', createShortURL, name='create'),
    path('reverse/', reverseURL, name='reverse'),
    path('<str:url>', redirect, name='redirect'),
   
]