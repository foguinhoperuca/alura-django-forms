from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('my_travels', views.my_travels, name='my_travels')
]
