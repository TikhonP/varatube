from django.urls import path
from .views import *

urlpatterns = [
    path('upload/', uploadp, name='uploadp'),
    path('', mainp, name='mainp'),
]
