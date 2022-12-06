from django.urls import path
from .views import home, createShortURL, redirect_original, reverseURL

urlpatterns = [
    path('', home, name='home'),
    path('create/', createShortURL, name='create'),
    path('reverse/', reverseURL, name='reverse'),
    path('<str:url>', redirect_original, name='redirect_original'),
   
]